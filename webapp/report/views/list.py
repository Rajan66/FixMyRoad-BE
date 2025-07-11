from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from serializers.report import ListReportSerializer
from utils.pagination import CustomPagination

from report.models import PotholeReport


class ListReportView(ListAPIView):
    serializer_class = ListReportSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPagination

    def get_queryset(self):
        user = self.request.user

        if not user.is_authenticated or user.role == "user":
            return PotholeReport.objects.all()

        if user.role == "admin":
            return PotholeReport.objects.all()

        if user.role == "ward":
            return PotholeReport.objects.filter(ward=user.ward)

        return PotholeReport.objects.all()


class ListMeReportView(ListAPIView):
    serializer_class = ListReportSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated and user.role == "user":
            print(user.profile)
            return PotholeReport.objects.filter(profile=user.profile)

        return PotholeReport.objects.none()
