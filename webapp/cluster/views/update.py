from rest_framework.generics import UpdateAPIView
from serializers.cluster import UpdateClusterSerializer

from cluster.models import Cluster


class UpdateClusterView(UpdateAPIView):
    serializer_class = UpdateClusterSerializer
    queryset = Cluster.objects.all()
