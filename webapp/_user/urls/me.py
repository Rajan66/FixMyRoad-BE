from django.urls import path

from _user.views import (
    CreateUserProfileView,
    DestroyUserProfileView,
    ListUserProfileView,
    RetrieveMeView,
    RetrieveUserProfileView,
    UpdateUserProfileView,
)

urlpatterns = [
    path(
        "update/<str:pk>/",
        UpdateUserProfileView.as_view(),
        name="update-profile",
    ),
    path(
        "delete/<str:pk>/",
        DestroyUserProfileView.as_view(),
        name="delete-profile",
    ),
    path(
        "retrieve/<str:pk>/",
        RetrieveUserProfileView.as_view(),
        name="retrieve-profile",
    ),
    path(
        "retrieve/",
        RetrieveMeView.as_view(),
        name="retrieve-me",
    ),
    path(
        "create/",
        CreateUserProfileView.as_view(),
        name="create-profile",
    ),
    path(
        "list/",
        ListUserProfileView.as_view(),
        name="list-profiles",
    ),
]
