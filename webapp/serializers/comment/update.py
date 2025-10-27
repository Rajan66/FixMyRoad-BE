from rest_framework import serializers

from comment.models import Comment


class CommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["comment"]

    def update(self, instance, validated_data):
        instance.comment = validated_data.get("comment", instance.comment)
        instance.save()
        return instance
