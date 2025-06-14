from django.urls import path

from _user.views import (
    CreateUserProfileView,
    DestroyUserProfileView,
    ListUserProfileView,
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
