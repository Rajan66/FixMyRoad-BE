from _algorithms.dbscan import dbscan
from _algorithms.utils import haversine
from cluster.models import Cluster
from report.models import PotholeReport as Report


def run_dbscan_clustering(eps=100, min_samples=2):
    # Unclustered reports: (id, lat, lon)
    reports = list(
        Report.objects.filter(cluster__isnull=True).values_list(
            "id", "latitude", "longitude"
        )
    )

    if not reports:
        print("No unclustered reports found.")
        return

    cluster_map = dbscan(
        reports, eps=eps, min_samples=min_samples, distance_func=haversine
    )

    from collections import defaultdict

    cluster_groups = defaultdict(list)
    for report_id, cid in cluster_map.items():
        if cid != -1:
            cluster_groups[cid].append(int(report_id))

    total_clusters = 0

    for cid, report_ids in cluster_groups.items():
        report_objs = list(Report.objects.filter(id__in=report_ids))

        if not report_objs:
            continue

        lat_avg = sum(r.latitude for r in report_objs) / len(report_objs)
        lon_avg = sum(r.longitude for r in report_objs) / len(report_objs)
        ward = report_objs[0].ward  # assuming same ward for all

        cluster = Cluster.objects.create(
            center_latitude=lat_avg,
            center_longitude=lon_avg,
            ward=ward,
        )

        # Assign reports to cluster
        for r in report_objs:
            r.cluster = cluster
            r.save(update_fields=["cluster"])

        # Set title
        report_count = len(report_objs)
        if ward:
            cluster.title = f"Cluster with {report_count} report{'s' if report_count > 1 else ''} in Ward {ward.number}"
        else:
            cluster.title = (
                f"Cluster with {report_count} report{'s' if report_count > 1 else ''}"
            )

        # Set metrics
        update_cluster_metrics(cluster)

        total_clusters += 1

    print(f"DBSCAN completed. {total_clusters} clusters created.")


def update_cluster_metrics(cluster):
    reports = cluster.reports.all()
    total = reports.count()
    valid = reports.filter(system_flag="valid").count()
    needs_review = reports.exclude(system_flag="valid").count()

    # system_flag
    if total == 0:
        cluster.system_flag = "needs_review"
    elif needs_review / total >= 0.5:
        cluster.system_flag = "needs_review"
    else:
        cluster.system_flag = "valid"

    # priority
    if total >= 10 and valid >= 7:
        cluster.priority = "high"
    elif total >= 5 and valid >= 3:
        cluster.priority = "medium"
    else:
        cluster.priority = "low"

    # Optional priority score (use if needed)
    # cluster.priority_score = valid + 0.5 * (total - valid)

    cluster.save()


def recluster_all_reports(eps=100, min_samples=2):
    print("Re-clustering all reports...")

    # clear existing clusters
    Report.objects.update(cluster=None)
    Cluster.objects.all().delete()

    reports = list(Report.objects.all().values_list("id", "latitude", "longitude"))
    if not reports:
        print("No reports found.")
        return

    cluster_map = dbscan(
        reports, eps=eps, min_samples=min_samples, distance_func=haversine
    )

    from collections import defaultdict

    cluster_groups = defaultdict(list)
    for report_id, cid in cluster_map.items():
        if cid != -1:
            cluster_groups[cid].append(int(report_id))

    total_clusters = 0

    # create clusters
    for cid, report_ids in cluster_groups.items():
        report_objs = list(Report.objects.filter(id__in=report_ids))
        if not report_objs:
            continue

        lat_avg = sum(r.latitude for r in report_objs) / len(report_objs)
        lon_avg = sum(r.longitude for r in report_objs) / len(report_objs)
        ward = report_objs[0].ward  # assume same ward

        cluster = Cluster.objects.create(
            center_latitude=lat_avg,
            center_longitude=lon_avg,
            ward=ward,
        )

        for r in report_objs:
            r.cluster = cluster
            r.save(update_fields=["cluster"])

        count = len(report_objs)
        if ward:
            cluster.title = (
                f"{count} report{'s' if count > 1 else ''} in Ward {ward.number}"
            )
        else:
            cluster.title = f"{count} report{'s' if count > 1 else ''}"

        update_cluster_metrics(cluster)
        total_clusters += 1

    print(f"Re-clustering complete. {total_clusters} clusters created.")
