from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from serializers.comment import CommentUpdateSerializer

from comment.models import Comment


class CommentUpdateView(UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentUpdateSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"

    def perform_update(self, serializer):
        comment = self.get_object()
        if comment.user != self.request.user:
            raise PermissionDenied("You do not have permission to edit this comment.")
        serializer.save()
