from django.urls import path

from _user.views import CreateUserView, ListUserView

urlpatterns = [
    path(
        "list/",
        ListUserView.as_view(),
        name="list-user",
    ),
    path(
        "register/",
        CreateUserView.as_view(),
        name="register",
    ),
]
