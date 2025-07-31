from _user.models import User
from django.contrib.auth.password_validation import validate_password
from django.db import transaction
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from ward.models import Ward


class CreateWardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = "__all__"

        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]


class RegisterWardSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        required=True,
    )

    ward_number = serializers.CharField(
        required=True,
    )

    address = serializers.CharField(
        required=False,
        allow_blank=True,
    )

    phone = serializers.CharField(
        required=False,
        allow_blank=True,
    )

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )

    role = serializers.CharField()

    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
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
        if attrs["role"] != "ward":
            raise serializers.ValidationError(
                {"role": "Only role 'ward' is allowed here."}
            )
        return attrs

    @transaction.atomic
    def create(self, validated_data: dict):
        ward_name = validated_data.pop("name")
        ward_number = validated_data.pop("ward_number")
        address = validated_data.pop("address", "")
        phone = validated_data.pop("phone", "")

        email = validated_data.pop("email")
        password = validated_data.pop("password")
        role = validated_data.pop("role")

        user_obj = User.objects.create_user(
            email=email,
            password=password,
            role=role,
        )

        ward_serializer = CreateWardSerializer(
            data={
                "name": ward_name,
                "ward_number": ward_number,
                "address": address,
                "phone": phone,
                "user": user_obj.id,
            }
        )
        ward_serializer.is_valid(raise_exception=True)
        ward = ward_serializer.save()

        return ward
