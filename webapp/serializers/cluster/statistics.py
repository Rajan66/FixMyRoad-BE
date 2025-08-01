from rest_framework import serializers

from cluster.models import Cluster


class StatisticsClusterSerializer(serializers.Serializer):
    open = serializers.SerializerMethodField()

    in_progress = serializers.SerializerMethodField()

    partially_resolved = serializers.SerializerMethodField()

    resolved = serializers.SerializerMethodField()

    def get_open(self, obj):
        return Cluster.objects.filter(status="open").count()

    def get_in_progress(self, obj):
        return Cluster.objects.filter(status="in_progress").count()

    def get_partially_resolved(self, obj):
        return Cluster.objects.filter(status="partially_resolved").count()

    def get_resolved(self, obj):
        return Cluster.objects.filter(status="resolved").count()
