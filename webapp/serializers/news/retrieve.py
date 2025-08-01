from rest_framework import serializers
from serializers.ward import ListWardSerializer

from news.models import News


class NewsRetrieveSerializer(serializers.ModelSerializer):
    ward = ListWardSerializer(read_only=True)
    author_name = serializers.CharField(source="author.name", read_only=True)

    class Meta:
        model = News
        fields = [
            "id",
            "title",
            "content",
            "image",
            "ward",
            "author_name",
            "created_at",
        ]
