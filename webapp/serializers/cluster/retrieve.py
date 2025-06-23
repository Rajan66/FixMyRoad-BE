from rest_framework import serializers

from cluster.models import Cluster


class RetrieveClusterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cluster
        fields = "__all__"
