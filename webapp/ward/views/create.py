from rest_framework.generics import CreateAPIView
from serializers.ward import CreateWardSerializer

from ward.models import Ward


class CreateWardView(CreateAPIView):
    serializer_class = CreateWardSerializer
    queryset = Ward.objects.all()
