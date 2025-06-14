from _user.models import UserProfile
from rest_framework import serializers


class UserProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile

        fields = "__all__"

        read_only = [
            "id",
            "created_at",
            "updated_at",
        ]

    def create(self, validated_data, **kwargs):
        print(validated_data)

        user = validated_data.pop("user")
        print(type(user))
        first_name = validated_data.pop("first_name")
        last_name = validated_data.pop("last_name")

        extra_context = {
            "bio": validated_data.pop("bio", ""),
            "address": validated_data.pop("address", ""),
            "phone": validated_data.pop("phone", ""),
            "image": validated_data.pop("image", None),
        }

        user_profile_obj = UserProfile.objects.create(
            user=user,
            first_name=first_name,
            last_name=last_name,
            **extra_context,
        )

        return user_profile_obj
