from rest_framework.generics import RetrieveAPIView
from serializers._profile import RetrieveUserProfileSerializer

from _user.models import UserProfile


class RetrieveUserProfileView(RetrieveAPIView):
    serializer_class = RetrieveUserProfileSerializer
    queryset = UserProfile.objects.all()
