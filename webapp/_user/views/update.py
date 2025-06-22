from rest_framework.generics import UpdateAPIView
from serializers._profile import UpdateUserProfileSerializer

from _user.models import UserProfile


class UpdateUserProfileView(UpdateAPIView):
    serializer_class = UpdateUserProfileSerializer
    queryset = UserProfile.objects.all()
