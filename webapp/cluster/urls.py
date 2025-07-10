from django.urls import path

from .views import (
    AllDBSCANView,
    CreateClusterView,
    DestroyClusterView,
    ListClusterView,
    ListWardClusterView,
    RetrieveClusterReportView,
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
        "list/ward/",
        ListWardClusterView.as_view(),
        name="list-ward-cluster",
    ),
    path(
        "retrieve/<str:pk>/",
        RetrieveClusterView.as_view(),
        name="retrieve-cluster",
    ),
    path(
        "retrieve/<str:pk>/reports/",
        RetrieveClusterReportView.as_view(),
        name="retrieve-cluster-reports",
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
    path(
        "dbscan/all/",
        AllDBSCANView.as_view(),
        name="run-dbscan-all",
    ),
]
