from rest_framework.response import Response
from rest_framework.views import APIView
from serializers.cluster import StatisticsClusterSerializer


class StatisticsClusterView(APIView):
    def get(self, request):
        serializer = StatisticsClusterSerializer(instance={})
        return Response(serializer.data)
