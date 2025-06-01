from rest_framework.generics import ListAPIView
from serializers._user import ListUserSerializer


class ListUserView(ListAPIView):
    serializer_class = ListUserSerializer
