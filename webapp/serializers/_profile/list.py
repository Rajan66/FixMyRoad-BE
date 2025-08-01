from _user.models import UserProfile
from rest_framework import serializers
from serializers._user import ListUserSerializer
from serializers.ward import ListWardSerializer


class ListUserProfileSerializer(serializers.ModelSerializer):
    user = ListUserSerializer()
    ward = ListWardSerializer()

    class Meta:
        model = UserProfile

        fields = "__all__"
