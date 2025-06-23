from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from serializers.report import RetrieveReportSerializer

from report.models import PotholeReport


class RetrieveReportView(RetrieveAPIView):
    serializer_class = RetrieveReportSerializer
    queryset = PotholeReport.objects.all()
    permission_classes = [AllowAny]
