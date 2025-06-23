from rest_framework.generics import UpdateAPIView
from serializers.ward import UpdateWardSerializer

from ward.models import Ward


class UpdateWardView(UpdateAPIView):
    serializer_class = UpdateWardSerializer
    queryset = Ward.objects.all()
