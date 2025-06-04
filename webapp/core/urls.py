from django.contrib import admin
from django.urls import include, path

api_prefix = "api/v1"
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("swagger.urls")),
    path(f"{api_prefix}/user/", include("_user.urls")),
    path(f"{api_prefix}/gatekeeper/", include("_gatekeeper.urls")),
]
