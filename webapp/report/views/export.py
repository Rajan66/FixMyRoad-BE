import csv

from django.http import HttpResponse
from rest_framework.views import APIView

from report.models import PotholeReport


class ExportReportView(APIView):
    def get(self, request):
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
            writer.writerow(
                [
                    report.ward.name,
                    report.ward.ward_number,
                    report.title,
                    report.description,
                    report.latitude,
                    report.longitude,
                    report.status,
                    report.severity,
                ]
            )

        return response
