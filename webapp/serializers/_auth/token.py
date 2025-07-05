from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


# FIX: this doesn't append first_name and last_name to token
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        profile = getattr(user, "profile", None)
        if profile:
            token["first_name"] = profile.first_name
            token["last_name"] = profile.last_name
        else:
            token["first_name"] = ""
            token["last_name"] = ""

        return token
