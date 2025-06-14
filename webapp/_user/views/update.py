from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from serializers._profile import UpdateUserProfileSerializer

from _user.models import UserProfile


class UpdateUserProfileView(UpdateAPIView):
    serializer_class = UpdateUserProfileSerializer
    queryset = UserProfile.objects.all()
    permission_classes = [IsAuthenticated]
