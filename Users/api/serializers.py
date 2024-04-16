from rest_framework.serializers import CharField, EmailField, Serializer, UUIDField


class NewUserSerializer(Serializer):
    email = EmailField(max_length=64)
    password = CharField(max_length=64)
    first_name = CharField(max_length=32)
    cart_id = UUIDField(required=False)


class ChangePasswordSerializer(Serializer):
    old_password = CharField(required=True)
    new_password = CharField(required=True)
