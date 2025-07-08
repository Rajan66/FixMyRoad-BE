from _user.models import User
from django.http import HttpResponse
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from utils.email_token import decode_verification_token


class VerifyEmailView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        token = request.GET.get("token")
        if not token:
            return HttpResponse("<h2>❌ Token missing.</h2>", status=400)

        try:
            data = decode_verification_token(token)
            user = User.objects.get(email=data["user_email"])
            if user.is_active:
                return HttpResponse("<h2>✅ Email already verified.</h2>")
            user.is_active = True
            user.save()
            return HttpResponse("<h2>🎉 Email successfully verified!</h2>")
        except Exception as e:
            return HttpResponse(
                f"<h2>❌ Verification failed: {str(e)}</h2>", status=400
            )
