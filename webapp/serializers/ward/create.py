from rest_framework import serializers

from ward.models import Ward


class CreateWardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = "__all__"

        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]
