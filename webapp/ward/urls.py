from django.urls import path

from .views import (
    CreateWardView,
    DestroyWardView,
    ListWardView,
    RetrieveMeWardView,
    RetrieveWardView,
    UpdateWardView,
)

urlpatterns = [
    path(
        "create/",
        CreateWardView.as_view(),
        name="create-ward",
    ),
    path(
        "list/",
        ListWardView.as_view(),
        name="list-ward",
    ),
    path(
        "retrieve/<str:pk>/",
        RetrieveWardView.as_view(),
        name="retrieve-ward",
    ),
    path(
        "me/retrieve/",
        RetrieveMeWardView.as_view(),
        name="retrieve-me-ward",
    ),
    path(
        "update/<str:pk>/",
        UpdateWardView.as_view(),
        name="update-ward",
    ),
    path(
        "delete/<str:pk>/",
        DestroyWardView.as_view(),
        name="delete-ward",
    ),
]
