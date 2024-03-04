from typing import ClassVar

from django.core.validators import MinValueValidator
from rest_framework.serializers import IntegerField, ModelSerializer, Serializer, SerializerMethodField, UUIDField

from cart.models import CartEntry


class ShoppingCartSerializer(ModelSerializer):
    product_name = SerializerMethodField()
    unit_price = SerializerMethodField()

    class Meta:
        model = CartEntry
        fields: ClassVar = [
            "product",
            "product_name",
            "quantity",
            "unit_price",
        ]

    def get_product_name(self, obj):
        return obj.product.name

    def get_unit_price(self, obj):
        return obj.product.price


class CartOperationSerializer(Serializer):
    amount = IntegerField(validators=[MinValueValidator(1)])
    product_id = UUIDField()
    cart_id = UUIDField()
