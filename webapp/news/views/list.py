from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from serializers.news import NewsListSerializer

from news.models import News


class NewsListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = News.objects.all()
    serializer_class = NewsListSerializer
