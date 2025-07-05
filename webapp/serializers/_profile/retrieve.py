from _user.models import UserProfile
from rest_framework import serializers


class RetrieveUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile

        fields = "__all__"


class RetrieveMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile

        fields = "__all__"
