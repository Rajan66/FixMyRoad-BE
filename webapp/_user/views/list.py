from rest_framework.generics import ListAPIView
from serializers._profile import ListUserProfileSerializer
from serializers._user import ListUserSerializer

from _user.models import User, UserProfile


class ListUserView(ListAPIView):
    serializer_class = ListUserSerializer
    queryset = User.objects.all()


class ListUserProfileView(ListAPIView):
    serializer_class = ListUserProfileSerializer
    queryset = UserProfile.objects.all()
