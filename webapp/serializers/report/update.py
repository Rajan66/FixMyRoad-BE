from _algorithms.utils import classify_pothole  # assuming this is your classifier
from rest_framework import serializers

from report.models import PotholeReport


class UpdateReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = PotholeReport
        fields = "__all__"
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]

    def update(self, instance, validated_data):
        image = validated_data.get("image", None)

        print(image)
        if image:
            try:
                label, prob = classify_pothole(image)
                validated_data["system_flag"] = (
                    "valid" if label == "pothole" and prob > 0.8 else "needs_review"
                )
            except Exception:
                validated_data["system_flag"] = "needs_review"

        return super().update(instance, validated_data)
