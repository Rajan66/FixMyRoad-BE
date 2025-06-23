from rest_framework.generics import DestroyAPIView

from cluster.models import Cluster


class DestroyClusterView(DestroyAPIView):
    queryset = Cluster.objects.all()
