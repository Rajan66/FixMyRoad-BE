from rest_framework import serializers
from serializers._user import ListUserSerializer

from ward.models import Ward


class RetrieveWardSerializer(serializers.ModelSerializer):
    user = ListUserSerializer()

    class Meta:
        model = Ward
        fields = "__all__"
