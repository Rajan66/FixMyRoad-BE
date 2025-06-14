from django.urls import include, path

from _user.urls import me, user

urlpatterns = [
    path("", include(user.urlpatterns)),
    path("me/", include(me.urlpatterns)),
]
