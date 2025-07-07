from _user.models import UserProfile
from rest_framework import serializers
from serializers._user import ListUserSerializer


class RetrieveUserProfileSerializer(serializers.ModelSerializer):
    user = ListUserSerializer()

    class Meta:
        model = UserProfile

        fields = "__all__"


class RetrieveMeSerializer(serializers.ModelSerializer):
    user = ListUserSerializer()

    class Meta:
        model = UserProfile

        fields = "__all__"
