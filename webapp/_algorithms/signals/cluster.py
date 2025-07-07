from cluster.models import Cluster
from django.db.models.signals import post_save
from django.dispatch import receiver
from report.models import PotholeReport as Report

from _algorithms.utils import haversine


@receiver(post_save, sender=Report)
def assign_cluster(sender, instance, created, **kwargs):
    if not created or instance.cluster:
        return

    threshold = 500  # meters

    for cluster in Cluster.objects.all():
        for other in cluster.reports.all():
            distance = haversine(
                instance.latitude, instance.longitude, other.latitude, other.longitude
            )
            if distance <= threshold:
                instance.cluster = cluster
                instance.save(update_fields=["cluster"])
                return

    new_cluster = Cluster.objects.create(
        center_latitude=instance.latitude, center_longitude=instance.longitude
    )
    instance.cluster = new_cluster
    instance.save(update_fields=["cluster"])
