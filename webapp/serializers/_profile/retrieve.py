from _user.models import UserProfile
from rest_framework import serializers
from serializers._user import ListUserSerializer
from serializers.ward import ListWardSerializer


class RetrieveUserProfileSerializer(serializers.ModelSerializer):
    ward = ListWardSerializer()
    user = ListUserSerializer()

    class Meta:
        model = UserProfile

        fields = "__all__"


class RetrieveMeSerializer(serializers.ModelSerializer):
    ward = ListWardSerializer()
    user = ListUserSerializer()

    class Meta:
        model = UserProfile

        fields = "__all__"
