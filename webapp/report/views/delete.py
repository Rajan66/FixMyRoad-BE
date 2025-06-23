from rest_framework.generics import DestroyAPIView

from report.models import PotholeReport


class DestroyReportView(DestroyAPIView):
    queryset = PotholeReport.objects.all()
