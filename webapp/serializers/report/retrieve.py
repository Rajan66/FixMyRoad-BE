from rest_framework import serializers

from report.models import PotholeReport


class RetrieveReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = PotholeReport
        fields = "__all__"
