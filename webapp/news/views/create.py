from rest_framework.generics import CreateAPIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from serializers.news import NewsCreateSerializer

from news.models import News


class NewsCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = News.objects.all()
    serializer_class = NewsCreateSerializer
    parser_classes = [MultiPartParser, FormParser]
