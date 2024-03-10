from django.core.validators import MaxLengthValidator, MinValueValidator, RegexValidator
from rest_framework.serializers import CharField, IntegerField, Serializer, UUIDField


class OrderSerializer(Serializer):
    city = CharField(validators=[MaxLengthValidator(50)])
    street = CharField(validators=[MaxLengthValidator(50)])
    house_number = IntegerField(validators=[MinValueValidator(1)])
    postal_code = CharField(validators=[RegexValidator(r"\d{2}-\d{3}")])  # works for Poland
    phone_number = CharField(validators=[MaxLengthValidator(12)])

    shopping_cart_id = UUIDField(required=False)
