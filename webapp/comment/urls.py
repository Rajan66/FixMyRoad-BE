from django.urls import path

from .views import (
    CommentCreateView,
    CommentListView,
    CommentRetrieveView,
    CommentUpdateView,
)

urlpatterns = [
    path(
        "list/",
        CommentListView.as_view(),
        name="comment-list",
    ),
    path(
        "create/",
        CommentCreateView.as_view(),
        name="comment-create",
    ),
    path(
        "<int:id>/",
        CommentRetrieveView.as_view(),
        name="comment-detail",
    ),
    path(
        "<int:id>/update/",
        CommentUpdateView.as_view(),
        name="comment-update",
    ),
]
