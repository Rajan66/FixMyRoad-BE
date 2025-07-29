from datetime import timedelta

from django.utils import timezone
from rest_framework import serializers

from report.models import PotholeReport


class ReportStatisticsSerializer(serializers.Serializer):
    total_reports = serializers.SerializerMethodField()

    resolved_reports = serializers.SerializerMethodField()

    reports_lastweek = serializers.SerializerMethodField()

    resolved_reports_lastweek = serializers.SerializerMethodField()

    in_progress_reports = serializers.SerializerMethodField()

    in_progress_reports_lastweek = serializers.SerializerMethodField()

    open_reports = serializers.SerializerMethodField()

    open_reports_lastweek = serializers.SerializerMethodField()

    def get_total_reports(self, obj):
        return PotholeReport.objects.count()

    def get_resolved_reports(self, obj):
        return PotholeReport.objects.filter(status="resolved").count()

    def get_reports_lastweek(self, obj):
        current_total = PotholeReport.objects.count()
        one_week_ago = timezone.now() - timedelta(weeks=1)
        total_week_ago = PotholeReport.objects.filter(
            created_at__lt=one_week_ago
        ).count()
        return current_total - total_week_ago

    def get_resolved_reports_lastweek(self, obj):
        current_resolved = PotholeReport.objects.filter(
            status="resolved",
        ).count()
        one_week_ago = timezone.now() - timedelta(weeks=1)
        resolved_week_ago = PotholeReport.objects.filter(
            status="resolved",
            updated_at__lt=one_week_ago,
        ).count()
        return current_resolved - resolved_week_ago

    def get_in_progress_reports(self, obj):
        return PotholeReport.objects.filter(status="in progress").count()

    def get_in_progress_reports_lastweek(self, obj):
        current_resolved = PotholeReport.objects.filter(
            status="in progress",
        ).count()
        one_week_ago = timezone.now() - timedelta(weeks=1)
        resolved_week_ago = PotholeReport.objects.filter(
            status="in progress",
            updated_at__lt=one_week_ago,
        ).count()
        return current_resolved - resolved_week_ago

    def get_open_reports(self, obj):
        return PotholeReport.objects.filter(status="open").count()

    def get_open_reports_lastweek(self, obj):
        current_resolved = PotholeReport.objects.filter(
            status="open",
        ).count()
        one_week_ago = timezone.now() - timedelta(weeks=1)
        resolved_week_ago = PotholeReport.objects.filter(
            status="open",
            updated_at__lt=one_week_ago,
        ).count()
        return current_resolved - resolved_week_ago
