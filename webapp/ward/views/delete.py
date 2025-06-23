from rest_framework.generics import DestroyAPIView

from ward.models import Ward


class DestroyWardView(DestroyAPIView):
    queryset = Ward.objects.all()
