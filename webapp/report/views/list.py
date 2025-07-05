from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from serializers.report import ListReportSerializer

from report.models import PotholeReport


class ListReportView(ListAPIView):
    serializer_class = ListReportSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user = self.request.user

        if not user.is_authenticated or user.role == "user":
            return PotholeReport.objects.all()

        if user.role == "admin":
            return PotholeReport.objects.all()

        if user.role == "ward":
            return PotholeReport.objects.filter(ward=user.profile.ward)

        return PotholeReport.objects.all()
