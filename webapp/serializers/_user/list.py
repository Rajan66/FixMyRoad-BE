from rest_framework import serializers

from _user.models import User


class ListUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = ["id", "email", "is_active", "role"]
