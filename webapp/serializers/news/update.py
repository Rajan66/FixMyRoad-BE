from rest_framework import serializers

from news.models import News


class NewsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = [
            "title",
            "content",
            "image",
            "ward",
        ]
