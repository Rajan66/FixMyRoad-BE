from datetime import timedelta

from django.db.models import Count
from django.utils import timezone
from rest_framework import serializers

from report.models import PotholeReport


class ReportStatisticsSerializer(serializers.Serializer):
    total_reports = serializers.IntegerField()
    resolved_reports = serializers.IntegerField()
    reports_lastweek = serializers.IntegerField()
    resolved_reports_lastweek = serializers.IntegerField()
    in_progress_reports = serializers.IntegerField()
    in_progress_reports_lastweek = serializers.IntegerField()
    open_reports = serializers.IntegerField()
    open_reports_lastweek = serializers.IntegerField()
    low_severity = serializers.IntegerField()
    medium_severity = serializers.IntegerField()
    high_severity = serializers.IntegerField()

    def to_representation(self, instance):
        now = timezone.now()
        one_week_ago = now - timedelta(weeks=1)

        all_reports = PotholeReport.objects.all()
        last_week_reports = all_reports.filter(created_at__gte=one_week_ago)
        updated_last_week = all_reports.filter(updated_at__gte=one_week_ago)

        # Prepare count map
        status_counts = all_reports.values("status").annotate(
            count=Count("id"),
        )
        severity_counts = all_reports.values("severity").annotate(
            count=Count("id"),
        )

        updated_status_counts = updated_last_week.values("status").annotate(
            count=Count("id")
        )

        # Convert to dicts
        status_map = {item["status"]: item["count"] for item in status_counts}
        severity_map = {item["severity"]: item["count"] for item in severity_counts}  # noqa
        updated_map = {item["status"]: item["count"] for item in updated_status_counts}  # noqa

        return {
            "total_reports": all_reports.count(),
            "resolved_reports": status_map.get("resolved", 0),
            "reports_lastweek": last_week_reports.count(),
            "resolved_reports_lastweek": updated_map.get("resolved", 0),
            "in_progress_reports": status_map.get("in progress", 0),
            "in_progress_reports_lastweek": updated_map.get("in progress", 0),
            "open_reports": status_map.get("open", 0),
            "open_reports_lastweek": updated_map.get("open", 0),
            "low_severity": severity_map.get("low", 0),
            "medium_severity": severity_map.get("medium", 0),
            "high_severity": severity_map.get("high", 0),
        }
