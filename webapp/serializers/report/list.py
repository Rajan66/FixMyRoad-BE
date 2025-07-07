from rest_framework import serializers

from report.models import PotholeReport


class ListReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = PotholeReport
        fields = "__all__"


class AutoBulkReportSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        return PotholeReport.objects.bulk_create(
            [PotholeReport(**attrs) for attrs in validated_data]
        )
