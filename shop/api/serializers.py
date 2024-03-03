import base64
from pathlib import Path
from typing import ClassVar

from django.conf import settings
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from shop.models import Product


class ProductSerializer(ModelSerializer):
    category = SerializerMethodField()

    class Meta:
        model = Product
        fields: ClassVar = "__all__"

    def get_category(self, obj):
        if obj.category:
            return obj.category.name
        return None
