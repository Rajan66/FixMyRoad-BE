from rest_framework import serializers
from serializers._profile import RetrieveUserProfileSerializer
from serializers.ward import ListWardSerializer

from report.models import PotholeReport


class RetrieveReportSerializer(serializers.ModelSerializer):
    ward = ListWardSerializer()
    profile = RetrieveUserProfileSerializer()

    class Meta:
        model = PotholeReport
        fields = "__all__"
