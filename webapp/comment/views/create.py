from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from serializers.comment import CommentCreateSerializer

from comment.models import Comment


class CommentCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
