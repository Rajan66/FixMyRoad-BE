from rest_framework import serializers
from serializers.report import ListReportSerializer

from cluster.models import Cluster


class ListClusterReportSerializer(serializers.ModelSerializer):
    reports = ListReportSerializer(many=True)

    class Meta:
        model = Cluster
        fields = "__all__"
