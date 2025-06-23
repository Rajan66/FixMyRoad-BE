from _user.models import UserProfile
from rest_framework import serializers


class ListUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile

        fields = "__all__"
