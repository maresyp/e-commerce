from typing import ClassVar

from django.core.validators import MinValueValidator
from rest_framework.serializers import IntegerField, ModelSerializer, Serializer, UUIDField

from cart.models import CartEntry


class ShoppingCartSerializer(ModelSerializer):
    class Meta:
        model = CartEntry
        fields: ClassVar = [
            "product",
            "quantity",
        ]


class CartOperationSerializer(Serializer):
    amount = IntegerField(validators=[MinValueValidator(1)])
    product_id = UUIDField()
    cart_id = UUIDField()
