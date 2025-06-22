from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import AllowAny

from _user.models import User, UserProfile


class DestroyUserView(DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class DestroyUserProfileView(DestroyAPIView):
    queryset = UserProfile.objects.all()
    permission_classes = [AllowAny]

    def perform_destroy(self, instance):
        user = instance.user
        instance.delete()
        user.delete()
