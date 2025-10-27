from rest_framework import serializers

from comment.models import Comment


class CommentListSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    report = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = [
            "id",
            "report",
            "user",
            "comment",
            "created_at",
        ]
