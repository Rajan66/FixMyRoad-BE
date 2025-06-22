from rest_framework.generics import RetrieveAPIView
from serializers.report import RetrieveReportSerializer

from report.models import PotholeReport


class RetrieveReportView(RetrieveAPIView):
    serializer_class = RetrieveReportSerializer
    queryset = PotholeReport.objects.all()
