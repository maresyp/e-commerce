from datetime import timedelta

from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from cart.models import CartEntry, ShoppingCart
from shop.models import Product

from .serializers import CartOperationSerializer, ShoppingCartSerializer


@api_view(["POST"])
def get_shopping_cart(request):
    if request.user.is_authenticated:
        shopping_cart, _created = ShoppingCart.objects.get_or_create(owner=request.user)
    else:
        shopping_cart, _created = ShoppingCart.objects.get_or_create(expiration_date=timezone.now() + timedelta(days=14))

    serializer = ShoppingCartSerializer(shopping_cart.cartentry_set.all(), many=True)

    return Response(serializer.data)


@api_view(["POST"])
def cart_add_product(request) -> Response:
    serializer = CartOperationSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    cart = get_object_or_404(ShoppingCart, pk=serializer.validated_data["cart_id"])
    if cart.owner is not None and cart.owner != request.user:
        return Response({"cart_id": ["You must be an owner of the cart to change it"]}, status=status.HTTP_403_FORBIDDEN)

    amount: int = serializer.validated_data["amount"]
    product = get_object_or_404(Product, pk=serializer.validated_data["product_id"])

    # check if the product is already in the cart
    if CartEntry.objects.filter(product=product, cart=cart).exists():
        entry = CartEntry.objects.get(product=product, cart=cart)
        entry.quantity += amount
    else:
        entry = CartEntry.objects.create(product=product, quantity=amount, cart=cart)

    entry.save()
    return Response()


@api_view(["POST"])
def cart_remove_product(request):
    pass
