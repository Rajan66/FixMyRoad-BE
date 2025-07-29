from rest_framework.response import Response
from rest_framework.views import APIView
from serializers.report import ReportStatisticsSerializer


class ReportStatisticsView(APIView):
    def get(self, request):
        serializer = ReportStatisticsSerializer(instance={})
        return Response(serializer.data)
