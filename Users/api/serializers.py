from typing import ClassVar

from rest_framework.serializers import CharField, EmailField, ModelSerializer, Serializer, UUIDField

from Users.models import Profile


class NewUserSerializer(Serializer):
    email = EmailField(max_length=64)
    password = CharField(max_length=64)
    first_name = CharField(max_length=32)
    cart_id = UUIDField(required=False)


class ChangePasswordSerializer(Serializer):
    old_password = CharField(required=True)
    new_password = CharField(required=True)


class ProfileUpdateSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields: ClassVar = ["gender", "city", "street", "house_number", "postal_code", "phone_number"]
