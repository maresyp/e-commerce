from typing import ClassVar

from rest_framework.serializers import ModelSerializer, SerializerMethodField

from shop.models import Product


class ProductSerializer(ModelSerializer):
    category = SerializerMethodField()
    product_image = SerializerMethodField()

    class Meta:
        model = Product
        fields: ClassVar = "__all__"

    def get_category(self, obj):
        if obj.category:
            return obj.category.name
        return None

    def get_product_image(self, _obj):
        return None
