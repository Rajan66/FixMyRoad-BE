from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from serializers._profile import RetrieveMeSerializer, RetrieveUserProfileSerializer

from _user.models import UserProfile


class RetrieveUserProfileView(RetrieveAPIView):
    serializer_class = RetrieveUserProfileSerializer
    queryset = UserProfile.objects.all()


class RetrieveMeView(RetrieveAPIView):
    serializer_class = RetrieveMeSerializer
    queryset = UserProfile.objects.all()

    def get(self, request, *args, **kwargs):
        profile = request.user.profile.first()
        if not profile:
            return Response({"detail": "Profile not found."}, status=404)

        serializer = self.get_serializer(profile)
        data = serializer.data.copy()
        data["role"] = request.user.role
        print(request.user.role)
        return Response(data)
