from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from serializers.report import CreateBulkReportSerializer

from report.models import PotholeReport


class CreateBulkReportView(CreateAPIView):
    serializer_class = CreateBulkReportSerializer
    queryset = PotholeReport.objects.all()

    def get_serializer(self, *args, **kwargs):
        # Handle schema generation case
        if (
            not hasattr(self, "request")
            or not self.request
            or not hasattr(self.request, "data")
        ):
            kwargs["many"] = True
            return super().get_serializer(*args, **kwargs)

        # Normal request processing
        if not isinstance(self.request.data, list):
            raise ValidationError(
                {"detail": "Expected a list of items for bulk creation."}
            )
        kwargs["many"] = True
        return super().get_serializer(*args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instances = serializer.save()
        response_serializer = self.get_serializer(instances, many=True)
        return Response(
            response_serializer.data,
            status=status.HTTP_201_CREATED,
        )
