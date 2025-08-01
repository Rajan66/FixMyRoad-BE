from base.enums import ClusterStatus
from cluster.models import Cluster
from django.db.models import Count
from rest_framework.response import Response
from rest_framework.views import APIView


class StatisticsWardClusterView(APIView):
    def get(self, request, pk):
        data = (
            Cluster.objects.filter(ward=pk)
            .values("status")
            .annotate(count=Count("status"))
        )

        # Step 1: Create a default dict with all statuses set to 0
        result = {status: 0 for status, _ in ClusterStatus.STATUS_CHOICES}

        # Step 2: Fill in actual counts from DB
        for item in data:
            result[item["status"]] = item["count"]

        return Response(result)
