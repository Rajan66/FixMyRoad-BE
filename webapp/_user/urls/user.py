from django.urls import path

from _user.views import CreateUserView, DestroyUserView, ListUserView

urlpatterns = [
    path(
        "list/",
        ListUserView.as_view(),
        name="list-user",
    ),
    path(
        "delete/<str:pk>/",
        DestroyUserView.as_view(),
        name="delete-user",
    ),
    path(
        "register/",
        CreateUserView.as_view(),
        name="register",
    ),
]
