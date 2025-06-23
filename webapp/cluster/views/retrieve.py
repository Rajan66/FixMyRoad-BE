from rest_framework.generics import RetrieveAPIView
from serializers.cluster import RetrieveClusterSerializer

from cluster.models import Cluster


class RetrieveClusterView(RetrieveAPIView):
    serializer_class = RetrieveClusterSerializer
    queryset = Cluster.objects.all()
