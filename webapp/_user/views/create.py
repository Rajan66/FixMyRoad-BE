from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from serializers._profile import CreateUserProfileSerializer
from serializers._user import CreateUserSerializer


class CreateUserView(CreateAPIView):
    serializer_class = CreateUserSerializer
    permission_classes = [
        AllowAny,
    ]


class CreateUserProfileView(CreateAPIView):
    serializer_class = CreateUserProfileSerializer
    permission_classes = [
        IsAuthenticated,
    ]
