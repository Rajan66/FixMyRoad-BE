from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from serializers.ward import ListWardSerializer

from ward.models import Ward


class ListWardView(ListAPIView):
    serializer_class = ListWardSerializer
    queryset = Ward.objects.all()
    permission_classes = [AllowAny]
    pagination_class = None
