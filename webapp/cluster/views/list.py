from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from serializers.cluster import ListClusterSerializer
from utils.pagination import CustomPagination

from cluster.models import Cluster


class ListClusterView(ListAPIView):
    serializer_class = ListClusterSerializer
    queryset = Cluster.objects.all()
    permission_classes = [AllowAny]
    pagination_class = CustomPagination


class ListWardClusterView(ListAPIView):
    serializer_class = ListClusterSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

    def get_queryset(self):
        user = self.request.user

        if user.role == "ward":
            print(user.ward.id)
            return Cluster.objects.filter(ward=user.ward)

        raise PermissionDenied("Invalid user role.")
