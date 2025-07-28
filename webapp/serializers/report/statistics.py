from datetime import timedelta

from django.utils import timezone
from rest_framework import serializers

from report.models import PotholeReport


class ReportCountSerializer(serializers.Serializer):
    total_reports = serializers.SerializerMethodField()
    total_resolved_reports = serializers.SerializerMethodField()
    reports_last_week = serializers.SerializerMethodField()
    resolved_reports_last_week = serializers.SerializerMethodField()

    def get_total_reports(self, obj):
        return PotholeReport.objects.count()

    def get_total_resolved_reports(self, obj):
        return PotholeReport.objects.filter(status="resolved").count()

    def get_reports_last_week(self, obj):
        # Get current counts
        current_total = PotholeReport.objects.count()

        # Get counts from 1 week ago
        one_week_ago = timezone.now() - timedelta(weeks=1)
        total_week_ago = PotholeReport.objects.filter(
            created_at__lt=one_week_ago
        ).count()

        # Return the difference (new reports in the last week)
        return current_total - total_week_ago

    def get_resolved_reports_last_week(self, obj):
        # Get current resolved count
        current_resolved = PotholeReport.objects.filter(status="resolved").count()

        # Get resolved count from 1 week ago
        one_week_ago = timezone.now() - timedelta(weeks=1)
        resolved_week_ago = PotholeReport.objects.filter(
            status="resolved",
            updated_at__lt=one_week_ago,  # Assuming resolved status is set via updated_at
        ).count()

        # Return the difference (newly resolved reports in the last week)
        return current_resolved - resolved_week_ago
