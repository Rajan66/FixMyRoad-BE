from rest_framework.generics import CreateAPIView
from serializers.report import CreateReportSerializer

from report.models import PotholeReport


class CreateReportView(CreateAPIView):
    serializer_class = CreateReportSerializer
    queryset = PotholeReport.objects.all()
