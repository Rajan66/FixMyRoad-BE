import csv

from django.http import HttpRequest, HttpResponse
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from report.models import PotholeReport


class ExportReportView(APIView):
    permission_classes = [AllowAny]

    def get(self, request: HttpRequest) -> HttpResponse:
        reports = PotholeReport.objects.filter(system_flag="valid")

        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="valid_reports.csv"'  # noqa

        writer = csv.writer(response)
        writer.writerow(
            [
                "Ward Name",
                "Ward Number",
                "Title",
                "Description",
                "Latitude",
                "Longitude",
                "Status",
                "Severity",
            ]
        )

        for report in reports:
            ward_name = report.ward.name if report.ward and report.ward.name else ""  # noqa
            ward_number = (
                report.ward.ward_number
                if report.ward and report.ward.ward_number
                else ""
            )

            writer.writerow(
                [
                    ward_name,
                    ward_number,
                    report.title or "",
                    report.description or "",
                    report.latitude or "",
                    report.longitude or "",
                    report.status or "",
                    report.severity or "",
                ]
            )

        return response
