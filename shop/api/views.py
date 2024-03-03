from pathlib import Path
from uuid import UUID

from django.http import FileResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from shop.models import Product

from .serializers import ProductSerializer


@api_view(["GET"])
def get_all_products(_request) -> Response:
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_product_image(_request, product_id: UUID) -> FileResponse:
    product = get_object_or_404(Product, pk=product_id)
    return FileResponse(Path(product.product_image.path).open("rb"), content_type="image/jpg")  # noqa: SIM115 file is closed automatically
