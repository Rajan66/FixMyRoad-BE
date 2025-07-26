from rest_framework import serializers

from report.models import PotholeReport


class ReportCountSerializer(serializers.Serializer):
    total_reports = serializers.SerializerMethodField()
    total_resolved_reports = serializers.SerializerMethodField()

    def get_total_reports(self, obj):
        return PotholeReport.objects.count()

    def get_total_resolved_reports(self, obj):
        return PotholeReport.objects.filter(status="resolved").count()
