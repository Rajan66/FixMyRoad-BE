from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from serializers.comment import CommentRetrieveSerializer

from comment.models import Comment


class CommentRetrieveView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentRetrieveSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = "id"
