from rest_framework.generics import ListAPIView
from serializers.report import ListReportSerializer

from report.models import PotholeReport


class ListReportView(ListAPIView):
    serializer_class = ListReportSerializer
    queryset = PotholeReport.objects.all()
