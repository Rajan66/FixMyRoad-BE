from cluster.models import Cluster
from django.db.models.signals import post_save
from django.dispatch import receiver
from report.models import PotholeReport as Report

from _algorithms.dbscan import dbscan
from _algorithms.utils import haversine


@receiver(post_save, sender=Report)
def assign_cluster(sender, instance, created, **kwargs):
    print("Clustering....")
    # Fetch all unclustered reports (including this one)
    unclustered = Report.objects.filter(cluster__isnull=True)
    if unclustered.count() < 2:
        # not enough reports to form a cluster; wait for more
        return

    # prepare (id, lat, lon)
    points = [(str(r.id), r.latitude, r.longitude) for r in unclustered]

    clustering_result = dbscan(
        points,
        eps=250,  # meters
        min_samples=2,
        distance_func=haversine,
    )

    # group reports by cluster ID (skip -1 noise)
    from collections import defaultdict

    cluster_groups = defaultdict(list)
    for report_id, cid in clustering_result.items():
        if cid != -1:
            cluster_groups[cid].append(report_id)

    # create clusters and assign reports
    for cid, report_ids in cluster_groups.items():
        reports = Report.objects.filter(id__in=report_ids)

        # compute center
        lat_avg = sum(r.latitude for r in reports) / len(reports)
        lon_avg = sum(r.longitude for r in reports) / len(reports)

        ward = reports.first().ward

        cluster = Cluster.objects.create(
            center_latitude=lat_avg,
            center_longitude=lon_avg,
            ward=ward,
        )

        reports.update(cluster=cluster)

        count = reports.count()
        if ward:
            cluster.title = f"Cluster with {count} report{'s' if count > 1 else ''} in Ward {ward.number}"
        else:
            cluster.title = f"Cluster with  {count} report{'s' if count > 1 else ''}"

        cluster.save()
        update_cluster_metrics(cluster)


def update_cluster_metrics(cluster):
    reports = cluster.reports.all()
    total = reports.count()
    valid = reports.filter(system_flag="valid").count()
    needs_review = reports.exclude(system_flag="valid").count()

    # set cluster.system_flag
    if total == 0:
        cluster.system_flag = "needs_review"
    elif needs_review / total >= 0.5:
        cluster.system_flag = "needs_review"
    else:
        cluster.system_flag = "valid"

    # Set cluster.priority
    if total >= 10 and valid >= 7:
        cluster.priority = "high"
    elif total >= 5 and valid >= 3:
        cluster.priority = "medium"
    else:
        cluster.priority = "low"

    print("Clustering complete...")
    cluster.save()
