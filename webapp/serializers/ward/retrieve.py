from rest_framework import serializers

from ward.models import Ward


class RetrieveWardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = "__all__"
