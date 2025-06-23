from rest_framework.generics import CreateAPIView
from serializers.cluster import CreateClusterSerializer

from cluster.models import Cluster


class CreateClusterView(CreateAPIView):
    serializer_class = CreateClusterSerializer
    queryset = Cluster.objects.all()
