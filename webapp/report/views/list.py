from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from serializers.report import ListReportSerializer

from report.models import PotholeReport


class ListReportView(ListAPIView):
    serializer_class = ListReportSerializer
    queryset = PotholeReport.objects.all()
    permission_classes = [AllowAny]
