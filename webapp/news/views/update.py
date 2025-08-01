from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from serializers.news import NewsUpdateSerializer

from news.models import News


class NewsUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = News.objects.all()
    serializer_class = NewsUpdateSerializer
