from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

api_prefix = "api/v1"
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("swagger.urls")),
    path(f"{api_prefix}/auth/", include("_auth.urls")),
    path(f"{api_prefix}/user/", include("_user.urls")),
    path(f"{api_prefix}/ward/", include("ward.urls")),
    path(f"{api_prefix}/gatekeeper/", include("_gatekeeper.urls")),
    path(f"{api_prefix}/report/", include("report.urls")),
    path(f"{api_prefix}/cluster/", include("cluster.urls")),
    path(f"{api_prefix}/comment/", include("comment.urls")),
    path(f"{api_prefix}/news/", include("news.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
