from rest_framework.generics import DestroyAPIView

from _user.models import User, UserProfile


class DestroyUserView(DestroyAPIView):
    queryset = User.objects.all()


class DestroyUserProfileView(DestroyAPIView):
    queryset = UserProfile.objects.all()

    def perform_destroy(self, instance):
        user = instance.user
        instance.delete()
        user.delete()
