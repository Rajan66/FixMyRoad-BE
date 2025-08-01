# cluster/views.py

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from services._algorithm.dbscan import (  # noqa
    recluster_all_reports,
    run_dbscan_clustering,
)


class AllDBSCANView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            # run_dbscan_clustering(eps=250, min_samples=2)
            recluster_all_reports(eps=250, min_samples=2)
            return Response(
                {"message": "DBSCAN clustering completed."}, status=status.HTTP_200_OK
            )

        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
