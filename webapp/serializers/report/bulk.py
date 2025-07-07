from rest_framework import serializers
from serializers.report.list import AutoBulkReportSerializer

from report.models import PotholeReport


class CreateBulkReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = PotholeReport
        fields = "__all__"
        list_serializer_class = AutoBulkReportSerializer

    def create(self, validated_data):
        return PotholeReport.objects.create(**validated_data)
