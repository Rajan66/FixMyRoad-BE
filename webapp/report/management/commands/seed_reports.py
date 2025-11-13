from django.utils import timezone
from datetime import timedelta
import os
import random
from django.core.files import File
from django.core.management.base import BaseCommand
from faker import Faker
from _user.models import UserProfile
from ward.models import Ward
from report.models import PotholeReport
from cluster.models import Cluster
from _algorithms.utils import classify_pothole
from base.enums.report import ReportChoices
from base.enums.cluster import ClusterStatus

# Paths to your image folders
POTHOLE_DIR = "/home/rajan/Projects/fixmyroad/predict_pothole/real_data/pothole"
NO_POTHOLE_DIR = "/home/rajan/Projects/fixmyroad/predict_pothole/real_data/no_pothole"

fake = Faker()

# Kathmandu coordinates bounds
LAT_MIN = 27.65
LAT_MAX = 27.78
LON_MIN = 85.28
LON_MAX = 85.35

TOTAL_REPORTS = 100
CLUSTER_COUNT = 20
REPORTS_PER_CLUSTER = 3
CLUSTER_OFFSET = 0.002  # ~250m

TITLES = [
    "Pothole on main road",
    "Broken pavement near park",
    "Road crack by school",
    "Damaged asphalt on street",
    "Sinkhole forming on road",
    "Uneven sidewalk tiles",
    "Large pothole near intersection",
    "Cracked road after rain",
    "Damaged road markings",
    "Waterlogged pothole",
    "Asphalt break by market",
    "Road erosion at curve",
    "Sidewalk damage near hospital",
    "Street hole causing traffic",
    "Road hazard reported",
    "Pothole near bus stop",
    "Damaged road by temple",
    "Street crack near mall",
    "Road damage reported",
    "Emergency road repair needed",
]

DESCRIPTIONS = [
    "This pothole has been causing vehicle damage and needs urgent repair.",
    "Residents have complained about the broken pavement in this area.",
    "Cracks in the road are increasing after rainfall.",
    "Dangerous hole in the street affecting daily commuters.",
    "Road surface is uneven and unsafe for two-wheelers.",
    "Large pothole making traffic slow in the morning.",
    "Minor road damage reported by locals; needs maintenance.",
    "Asphalt is broken, exposing underlying rocks.",
    "Street hole filled with water after rains; hazardous.",
    "Pothole causing accidents for cyclists.",
    "Sidewalk cracked, pedestrians at risk of falling.",
    "Emergency repair required; hole has expanded over weeks.",
    "Road condition deteriorating; needs municipal attention.",
    "Local shops complain about decreased foot traffic due to road damage.",
    "Water accumulation worsens pothole size.",
    "Temporary markings are fading; repair needed.",
    "Cracks forming along the road edges.",
    "Hole is deep and causing vehicle alignment issues.",
    "Traffic diversion suggested due to road hazard.",
    "Municipal team alerted for urgent road maintenance.",
]


def random_kathmandu_coords():
    lat = round(random.uniform(LAT_MIN, LAT_MAX), 6)
    lon = round(random.uniform(LON_MIN, LON_MAX), 6)
    return lat, lon


def random_past_datetime(days=90):
    """Return a random datetime within the past `days` days"""
    end_date = timezone.now()
    start_date = end_date - timedelta(days=days)
    return start_date + timedelta(
        seconds=random.randint(0, int((end_date - start_date).total_seconds()))
    )


class Command(BaseCommand):
    help = "Seed 100 pothole reports with clustering and image classification"

    def handle(self, *args, **kwargs):
        self.stdout.write("⚠️ Clearing existing reports and clusters...")
        PotholeReport.objects.all().delete()
        Cluster.objects.all().delete()

        profiles = list(UserProfile.objects.all())
        wards = list(Ward.objects.all())

        if not profiles or not wards:
            self.stdout.write(self.style.ERROR(
                "Seed UserProfiles and Wards first."))
            return

        # Load images
        pothole_images = [
            os.path.join(POTHOLE_DIR, f)
            for f in os.listdir(POTHOLE_DIR)
            if f.lower().endswith(("jpg", "jpeg", "png"))
        ]
        no_pothole_images = [
            os.path.join(NO_POTHOLE_DIR, f)
            for f in os.listdir(NO_POTHOLE_DIR)
            if f.lower().endswith(("jpg", "jpeg", "png"))
        ]

        if not pothole_images or not no_pothole_images:
            self.stdout.write(self.style.ERROR(
                "No images found in one of the folders"))
            return

        created_reports = []

        def create_report(image_path, ward, profile):
            lat, lon = random_kathmandu_coords()
            with open(image_path, "rb") as f:
                img_file = File(f)
                try:
                    label, prob = classify_pothole(img_file)
                    system_flag = (
                        "valid" if label == "pothole" and prob > 0.8 else "needs_review"
                    )
                    severity = (
                        random.choice([s[0]
                                      for s in ReportChoices.SEVERITY_CHOICES])
                        if label == "pothole"
                        else "low"
                    )
                except Exception:
                    system_flag = "needs_review"
                    severity = "low"

                random_created_at = random_past_datetime(90)

                report = PotholeReport.objects.create(
                    profile=profile,
                    ward=ward,
                    title=random.choice(TITLES),
                    description=random.choice(DESCRIPTIONS),
                    latitude=lat,
                    longitude=lon,
                    status=random.choice(
                        [s[0] for s in ReportChoices.STATUS_CHOICES]),
                    severity=severity,
                    system_flag=system_flag,
                    created_at=random_created_at,
                    updated_at=random_created_at,
                )
                report.image.save(os.path.basename(
                    image_path), img_file, save=True)
            return report

        # Create potholes (70%)
        for _ in range(int(TOTAL_REPORTS * 0.7)):
            report = create_report(
                random.choice(pothole_images),
                random.choice(wards),
                random.choice(profiles),
            )
            created_reports.append(report)

        # Create no potholes (30%)
        for _ in range(int(TOTAL_REPORTS * 0.3)):
            report = create_report(
                random.choice(no_pothole_images),
                random.choice(wards),
                random.choice(profiles),
            )
            created_reports.append(report)

        # --- Create clusters ---
        # Only cluster potholes, 3 per cluster, ~250m apart
        pothole_reports = [
            r for r in created_reports if r.system_flag == "valid"]
        random.shuffle(pothole_reports)

        cluster_count = 0
        i = 0
        while i + 2 < len(pothole_reports):
            cluster_reports = pothole_reports[i: i + 3]
            lat_center = sum(r.latitude for r in cluster_reports) / 3
            lon_center = sum(r.longitude for r in cluster_reports) / 3

            cluster = Cluster.objects.create(
                center_latitude=lat_center,
                center_longitude=lon_center,
                ward=random.choice(wards),
                status=ClusterStatus.STATUS_CHOICES[0][0],
                priority=ClusterStatus.PRIORITY_CHOICES[0][0],
                system_flag=ClusterStatus.FLAG_CHOICES[1][0],
            )

            for r in cluster_reports:
                # adjust coords slightly around center
                r.latitude = lat_center + random.uniform(-0.001, 0.001)
                r.longitude = lon_center + random.uniform(-0.001, 0.001)
                r.cluster = cluster
                r.save()

            cluster_count += 1
            i += 3

        self.stdout.write(
            self.style.SUCCESS(
                f"🎉 Created {len(created_reports)} reports and "
                + f"{cluster_count} clusters!"
            )
        )
