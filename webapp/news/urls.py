from django.urls import path

from .views import (
    NewsCreateView,
    NewsListView,
    NewsRetrieveView,
    NewsUpdateView,
)

urlpatterns = [
    path(
        "list/",
        NewsListView.as_view(),
        name="news-list",
    ),
    path(
        "create/",
        NewsCreateView.as_view(),
        name="news-create",
    ),
    path(
        "retrieve/<uuid:pk>/",
        NewsRetrieveView.as_view(),
        name="news-retrieve",
    ),
    path(
        "update/<uuid:pk>/",
        NewsUpdateView.as_view(),
        name="news-update-delete",
    ),
]
