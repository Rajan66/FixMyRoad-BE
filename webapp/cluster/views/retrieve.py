from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from serializers.cluster import ListClusterReportSerializer, RetrieveClusterSerializer

from cluster.models import Cluster


class RetrieveClusterView(RetrieveAPIView):
    serializer_class = RetrieveClusterSerializer
    queryset = Cluster.objects.all()
    permission_classes = [AllowAny]


class RetrieveClusterReportView(RetrieveAPIView):
    serializer_class = ListClusterReportSerializer
    queryset = Cluster.objects.all()
    permission_classes = [AllowAny]
