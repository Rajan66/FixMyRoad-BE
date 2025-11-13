from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from serializers.comment import CommentListSerializer
from comment.models import Comment


class CommentListView(ListAPIView):
    serializer_class = CommentListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        report_id = self.kwargs["report_id"]
        return Comment.objects.filter(report_id=report_id)
