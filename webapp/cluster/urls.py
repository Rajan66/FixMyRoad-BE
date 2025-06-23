from django.urls import path

from .views import (
    CreateClusterView,
    DestroyClusterView,
    ListClusterView,
    RetrieveClusterView,
    UpdateClusterView,
)

urlpatterns = [
    path(
        "create/",
        CreateClusterView.as_view(),
        name="create-cluster",
    ),
    path(
        "list/",
        ListClusterView.as_view(),
        name="list-cluster",
    ),
    path(
        "retrieve/<str:pk>/",
        RetrieveClusterView.as_view(),
        name="retrieve-cluster",
    ),
    path(
        "update/<str:pk>/",
        UpdateClusterView.as_view(),
        name="update-cluster",
    ),
    path(
        "delete/<str:pk>/",
        DestroyClusterView.as_view(),
        name="delete-cluster",
    ),
]
