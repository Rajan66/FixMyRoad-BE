from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from serializers.news import NewsListSerializer

from news.models import News


class NewsListView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = News.objects.all()
    serializer_class = NewsListSerializer
