from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import AllowAny

from _user.models import UserProfile


class DestroyUserProfileView(DestroyAPIView):
    queryset = UserProfile.objects.all()
    permission_classes = [AllowAny]
