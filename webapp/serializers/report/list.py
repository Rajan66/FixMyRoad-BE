from rest_framework import serializers

from report.models import PotholeReport


class ListReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = PotholeReport
        fields = "__all__"
