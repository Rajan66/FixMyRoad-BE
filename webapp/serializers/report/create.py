from rest_framework import serializers

from report.models import PotholeReport


class CreateReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = PotholeReport
        fields = "__all__"

        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]

    def create(self, validated_data):
        report = PotholeReport.objects.create(**validated_data)
        return report
