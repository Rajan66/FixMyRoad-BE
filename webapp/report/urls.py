from django.urls import path

from .views import (
    CreateReportView,
    DestroyReportView,
    ListReportView,
    RetrieveReportView,
    UpdateReportView,
)

urlpatterns = [
    path(
        "create/",
        CreateReportView.as_view(),
        name="create-report",
    ),
    path(
        "list/",
        ListReportView.as_view(),
        name="list-report",
    ),
    path(
        "retrieve/<str:pk>/",
        RetrieveReportView.as_view(),
        name="retrieve-report",
    ),
    path(
        "update/<str:pk>/",
        UpdateReportView.as_view(),
        name="update-report",
    ),
    path(
        "delete/<str:pk>/",
        DestroyReportView.as_view(),
        name="delete-report",
    ),
]
