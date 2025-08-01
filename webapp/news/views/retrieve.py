from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from serializers.news import NewsRetrieveSerializer

from news.models import News


class NewsRetrieveView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = News.objects.all()
    serializer_class = NewsRetrieveSerializer
