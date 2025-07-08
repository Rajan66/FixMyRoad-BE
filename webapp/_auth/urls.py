from django.urls import path

from _auth.views import VerifyEmailView

urlpatterns = [
    path("verify-email/", VerifyEmailView.as_view(), name="verify-email"),
]
