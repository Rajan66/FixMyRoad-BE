from _user.models import UserProfile
from rest_framework import serializers


class UpdateUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile

        fields = "__all__"

        read_only = [
            "id",
            "created_at",
            "updated_at",
        ]
