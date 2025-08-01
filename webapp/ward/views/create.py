from rest_framework.generics import CreateAPIView
from serializers.ward import CreateWardSerializer, RegisterWardSerializer

from ward.models import Ward


class CreateWardView(CreateAPIView):
    serializer_class = CreateWardSerializer
    queryset = Ward.objects.all()


class RegisterWardView(CreateAPIView):
    serializer_class = RegisterWardSerializer
    queryset = Ward.objects.all()
