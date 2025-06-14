from django.contrib.auth.password_validation import validate_password
from django.db import transaction
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from serializers._profile import CreateUserProfileSerializer

from _user.models import User


class CreateUserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(
        required=True,
        write_only=True,
    )

    last_name = serializers.CharField(
        required=True,
        write_only=True,
    )

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )

    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
    )

    password2 = serializers.CharField(
        write_only=True,
        required=True,
    )

    class Meta:
        model = User

        fields = "__all__"

        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
            "is_active",
        ]

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password2": "Password fields don't match."}
            )
        return attrs

    @transaction.atomic
    def create(self, validated_data: dict):
        validated_data.pop("password2")
        email = validated_data.pop("email")
        password = validated_data.pop("password")

        profile_data = {
            "first_name": validated_data.pop("first_name"),
            "last_name": validated_data.pop("last_name"),
        }

        user_obj = User.objects.create_user(email, password)

        profile_serializer = CreateUserProfileSerializer(
            data={**profile_data, "user": user_obj.id}
        )
        profile_serializer.is_valid(raise_exception=True)
        profile_serializer.save()

        print(profile_serializer)

        return user_obj
