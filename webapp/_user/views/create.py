from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from serializers._user import CreateUserSerializer


class CreateUserView(CreateAPIView):
    serializer_class = CreateUserSerializer
    permission_classes = [
        AllowAny,
    ]
