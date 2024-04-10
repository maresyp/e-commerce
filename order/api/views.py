from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from cart.models import ShoppingCart
from order.models import Order, OrderEntry

from .serializers import OrderSerializer


@api_view(["POST"])
def create_order(request) -> Response:
    serializer = OrderSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.user.is_authenticated:
        cart = get_object_or_404(ShoppingCart, owner=request.user)
    else:
        if "shopping_cart_id" not in serializer.validated_data:
            return Response({"shopping_cart_id": ["This field is required for not logged in users"]}, status=status.HTTP_400_BAD_REQUEST)

        cart = get_object_or_404(ShoppingCart, pk=serializer.validated_data["shopping_cart_id"])
        if cart.owner is not None:
            return Response({"shopping_cart_id": ["This shopping card belongs to someone else"]}, status=status.HTTP_403_FORBIDDEN)

    new_order = Order.objects.create(
        owner=request.user if request.user.is_authenticated else None,
        city=serializer.validated_data["city"],
        street=serializer.validated_data["street"],
        house_number=serializer.validated_data["house_number"],
        postal_code=serializer.validated_data["postal_code"],
        phone_number=serializer.validated_data["phone_number"],
    )

    for product in cart.cartentry_set.all():
        OrderEntry.objects.create(order=new_order, product=product.product, quantity=product.quantity)

    cart.cartentry_set.all().delete()

    return Response(status=status.HTTP_201_CREATED)
