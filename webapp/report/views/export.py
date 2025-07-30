import csv

from django.http import HttpResponse
from rest_framework.views import APIView

from report.models import PotholeReport


class ExportReportView(APIView):
    def get(self, request):
        reports = PotholeReport.objects.filter(system_flag="valid")

        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="valid_reports.csv"'

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
                "Image",
            ]
        )

        for report in reports:
            writer.writerow(
                [
                    report.ward.name if report.ward else "",
                    report.ward.ward_number if report.ward else "",
                    report.title,
                    report.description,
                    report.latitude,
                    report.longitude,
                    report.status,
                    report.severity,
                    report.image.url if report.image else "",
                ]
            )

        return response
