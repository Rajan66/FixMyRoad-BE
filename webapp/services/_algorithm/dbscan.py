from _algorithms.dbscan import dbscan
from _algorithms.utils import haversine
from cluster.models import Cluster
from report.models import PotholeReport as Report


def run_dbscan_clustering(eps=100, min_samples=2):
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

    # track cluster objects
    cid_to_cluster = {}

    for report_id, cid in cluster_map.items():
        if cid == -1:
            continue  # Skip noise
        if cid not in cid_to_cluster:
            # Create new Cluster
            report = Report.objects.get(id=report_id)
            cluster = Cluster.objects.create(
                center_latitude=report.latitude, center_longitude=report.longitude
            )
            cid_to_cluster[cid] = cluster
        else:
            cluster = cid_to_cluster[cid]

        # Assign report to cluster
        report = Report.objects.get(id=report_id)
        report.cluster = cluster
        report.save(update_fields=["cluster"])

    print(f"DBSCAN completed. {len(cid_to_cluster)} clusters created.")
