# import numpy as np
# from cluster.models import Cluster
# from report.models import Report
# from sklearn.cluster import DBSCAN
#
#
# def cluster_reports(eps_meters=100, min_samples=1):
#     reports = Report.objects.filter(cluster__isnull=True)
#     if not reports:
#         return
#
#     coords = np.array([[r.latitude, r.longitude] for r in reports])
#     coords_rad = np.radians(coords)
#
#     # eps in radians: meters / Earth's radius (6371000m)
#     eps_rad = eps_meters / 6371000.0
#
#     db = DBSCAN(eps=eps_rad, min_samples=min_samples, metric="haversine")
#     labels = db.fit_predict(coords_rad)
#
#     label_to_cluster = {}
#
#     for report, label in zip(reports, labels):
#         if label == -1:
#             # Noise → create new cluster
#             cluster = Cluster.objects.create()
#         elif label in label_to_cluster:
#             cluster = label_to_cluster[label]
#         else:
#             cluster = Cluster.objects.create()
#             label_to_cluster[label] = cluster
#
#         report.cluster = cluster
#         report.save()
