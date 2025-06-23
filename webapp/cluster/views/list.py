from rest_framework.generics import ListAPIView
from serializers.cluster import ListClusterSerializer

from cluster.models import Cluster


class ListClusterView(ListAPIView):
    serializer_class = ListClusterSerializer
    queryset = Cluster.objects.all()
