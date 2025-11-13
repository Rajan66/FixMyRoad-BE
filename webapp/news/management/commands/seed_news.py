import os
import random
from django.core.files import File
from django.core.management.base import BaseCommand
from ward.models import Ward
from news.models import News

POTHOLE_DIR = "/home/rajan/Projects/fixmyroad/predict_pothole/real_data/pothole"


class Command(BaseCommand):
    help = "Seed news items using pothole images, authored by ward users"

    def handle(self, *args, **kwargs):
        self.stdout.write("⚠️ Clearing existing news...")
        News.objects.all().delete()

        wards = list(Ward.objects.all())
        if not wards:
            self.stdout.write(self.style.ERROR("Seed Wards first."))
            return

        # Load pothole images
        pothole_images = [
            os.path.join(POTHOLE_DIR, f)
            for f in os.listdir(POTHOLE_DIR)
            if f.lower().endswith(("jpg", "jpeg", "png"))
        ]
        if not pothole_images:
            self.stdout.write(self.style.ERROR("No pothole images found!"))
            return

        # --- Predefined titles and longer contents ---
        predefined_news = [
            (
                "Massive Pothole Disrupts Morning Traffic",
                "A massive pothole appeared overnight near the main intersection, bringing early morning traffic to a standstill. "
                "Commuters reported vehicles swerving dangerously to avoid the damaged section, causing congestion that lasted for hours. "
                "Local shopkeepers claim the issue had been forming for weeks but went unnoticed by the authorities. "
                "City engineers have been dispatched to assess the damage and plan emergency repairs.",
            ),
            (
                "Ward 5 Faces Repeated Road Damage After Heavy Rainfall",
                "Continuous rainfall over the past week has once again exposed the poor drainage system in Ward 5. "
                "Residents complain that newly repaired roads have already started crumbling, leaving multiple potholes in less than a month. "
                "Motorcyclists are particularly affected, with several minor accidents reported during nighttime rides. "
                "Local authorities have promised to send maintenance crews, but no timeline has been given yet.",
            ),
            (
                "Local Youth Group Volunteers to Repair Minor Potholes",
                "Tired of waiting for municipal action, a youth group in the area organized a volunteer campaign to repair small potholes using available materials. "
                "Their initiative has received wide praise from locals, who see it as a sign of growing community involvement. "
                "While the repairs are temporary, the group hopes their efforts will push the government to take faster action on road maintenance.",
            ),
            (
                "Driver Injured After Losing Control Due to Unseen Pothole",
                "An early morning accident occurred near the riverside road when a driver lost control of his scooter after hitting a deep pothole. "
                "Witnesses reported that the area had no streetlights or warning signs, making it nearly invisible in the dark. "
                "The injured driver was taken to a nearby hospital and is now recovering. "
                "Residents have demanded reflective markers and immediate repairs to prevent further accidents.",
            ),
            (
                "Citizens Demand Urgent Action on Road Repairs",
                "Frustration is boiling over as residents across several wards voice complaints about deteriorating road conditions. "
                "Petitions have been submitted to municipal offices urging the government to prioritize road infrastructure budgets. "
                "Activists claim that poor roads are not only causing vehicle damage but also posing serious safety risks to pedestrians and schoolchildren.",
            ),
            (
                "Temporary Road Fix Crumbles Within a Week",
                "The freshly patched road section in Ward 8 has already started disintegrating, disappointing residents who hoped for a lasting repair. "
                "Locals report that the patchwork was done hastily without proper base reinforcement. "
                "Experts warn that such short-term fixes only waste public funds and call for better oversight in municipal contracts.",
            ),
            (
                "Complaints Surge on FixMyRoad App as Conditions Worsen",
                "The FixMyRoad app has seen a record number of pothole reports this month, signaling a growing concern among city residents. "
                "Most complaints come from wards affected by post-monsoon erosion. "
                "Developers of the platform said they are analyzing data clusters to identify the worst-affected areas for immediate attention.",
            ),
            (
                "Ward Representative Promises Swift Infrastructure Upgrades",
                "Responding to citizen pressure, the ward representative announced a new maintenance schedule to tackle long-standing road issues. "
                "The plan includes inspecting drainage systems, applying better asphalt mixtures, and ensuring quality control during repairs. "
                "Residents are cautiously optimistic but demand transparent updates and strict deadlines.",
            ),
            (
                "Elderly Resident Injured on Cracked Pavement",
                "A 70-year-old man was injured after tripping over a broken section of pavement outside his home. "
                "Neighbors claim the walkway has been in poor condition for months despite multiple complaints. "
                "The incident has reignited calls for the city to prioritize pedestrian safety, especially for senior citizens.",
            ),
            (
                "Community to Launch Awareness Drive for Road Safety",
                "Local NGOs and student groups are collaborating to host a road safety awareness campaign this weekend. "
                "The event aims to educate residents about the importance of reporting potholes and following traffic safety practices. "
                "Participants will also distribute flyers highlighting how community vigilance can help reduce accidents.",
            ),
        ]

        # --- Create News ---
        news_count = 0
        for ward in wards:
            if not ward.user:
                continue

            num_news = random.randint(1, 3)
            for _ in range(num_news):
                title, content = random.choice(predefined_news)
                image_path = random.choice(pothole_images)

                with open(image_path, "rb") as f:
                    img_file = File(f)
                    news_item = News.objects.create(
                        author=ward.user,
                        ward=ward,
                        title=title,
                        content=content,
                    )
                    news_item.image.save(
                        os.path.basename(image_path), img_file, save=True
                    )
                    news_count += 1

        self.stdout.write(self.style.SUCCESS(
            f"🎉 Created {news_count} news items!"))
