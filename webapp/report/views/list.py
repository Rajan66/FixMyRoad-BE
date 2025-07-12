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
        get_all_flag = self.request.query_params.get("getAll")

        if get_all_flag:
            return PotholeReport.objects.all().order_by("-updated_at")

        if not user.is_authenticated or user.role == "user":
            return PotholeReport.objects.all().order_by("-updated_at")

        if user.role == "admin":
            return PotholeReport.objects.all().order_by("-updated_at")

        if user.role == "ward":
            return PotholeReport.objects.filter(ward=user.ward).order_by("-updated_at")

        return PotholeReport.objects.all().order_by("-updated_at")


class ListMeReportView(ListAPIView):
    serializer_class = ListReportSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPagination

    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated and user.role == "user":
            return PotholeReport.objects.filter(profile=user.profile).order_by(
                "-updated_at"
            )

        return PotholeReport.objects.none()
