from django.urls import include, path

from _user.urls import user

urlpatterns = [path("", include(user.urlpatterns))]
