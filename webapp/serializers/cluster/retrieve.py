from rest_framework import serializers
from serializers.report import ListReportSerializer
from serializers.ward import RetrieveWardSerializer

from cluster.models import Cluster


class RetrieveClusterSerializer(serializers.ModelSerializer):
    reports = ListReportSerializer(many=True)
    ward = RetrieveWardSerializer()

    class Meta:
        model = Cluster
        fields = "__all__"
