from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from serializers.ward import RetrieveWardSerializer

from ward.models import Ward


class RetrieveWardView(RetrieveAPIView):
    serializer_class = RetrieveWardSerializer
    queryset = Ward.objects.all()
    permission_classes = [AllowAny]


class RetrieveMeWardView(RetrieveAPIView):
    serializer_class = RetrieveWardSerializer
    queryset = Ward.objects.all()

    def get_queryset(self):
        return Ward.objects.filter(user=self.request.user)
