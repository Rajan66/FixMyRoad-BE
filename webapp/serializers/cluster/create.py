from rest_framework import serializers

from cluster.models import Cluster


class CreateClusterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cluster
        fields = "__all__"

        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]
