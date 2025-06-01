from django.urls import path

from _user.views.list import ListUserView

urlpatterns = [
    path(
        "list/",
        ListUserView.as_view(),
        name="list-user",
    )
]
