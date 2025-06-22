from rest_framework.generics import UpdateAPIView
from serializers.report import UpdateReportSerializer

from report.models import PotholeReport


class UpdateReportView(UpdateAPIView):
    serializer_class = UpdateReportSerializer
    queryset = PotholeReport.objects.all()
