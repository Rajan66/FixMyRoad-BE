from rest_framework.response import Response
from rest_framework.views import APIView
from serializers.report import ReportCountSerializer


class ReportCountView(APIView):
    def get(self, request):
        serializer = ReportCountSerializer(instance={})
        return Response(serializer.data)
