from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from report.models import PotholeReport


@receiver(post_save, sender=PotholeReport)
def update_cluster_status_on_report_change(sender, instance, **kwargs):
    cluster = instance.cluster
    if not cluster:
        return

    def update_status():
        reports = PotholeReport.objects.filter(cluster=cluster)
        total = reports.count()
        if total == 0:
            cluster.status = "new"
            cluster.save()
            return

        resolved_count = reports.filter(status="resolved").count()
        in_progress_count = reports.filter(status="in_progress").count()

        if in_progress_count > 0:
            cluster.status = "in_progress"
        elif resolved_count == total:
            cluster.status = "resolved"
        elif resolved_count >= total / 2:
            cluster.status = "partially_resolved"
        else:
            cluster.status = "open"

        cluster.save()

    transaction.on_commit(update_status)
