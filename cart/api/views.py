from datetime import timedelta

from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, PermissionDenied

from cart.models import CartEntry, ShoppingCart
from shop.models import Product

from .serializers import CartOperationSerializer, ShoppingCartSerializer


@api_view(["GET"])
def get_shopping_cart(request):
    if request.user.is_authenticated:
        shopping_cart, _created = ShoppingCart.objects.get_or_create(owner=request.user)
    else:
        shopping_cart, _created = ShoppingCart.objects.get_or_create(expiration_date=timezone.now() + timedelta(days=14))

    serializer = ShoppingCartSerializer(shopping_cart.cartentry_set.all(), many=True)
    amount_of_products: int = len(serializer.data)
    total_price: float = 0.0

    for product in serializer.data:
        total_price += product["unit_price"] * product["quantity"]

    return Response(
        {
            "cart_id": shopping_cart.id,
            "amount_of_products": amount_of_products,
            "total_price": total_price,
            "entries": serializer.data,
        },
    )


def deserialize_cart_data(request):
    serializer = CartOperationSerializer(data=request.data)
    if not serializer.is_valid():
        raise ValidationError(serializer.errors)

    cart = get_object_or_404(ShoppingCart, pk=serializer.validated_data["cart_id"])
    if cart.owner is not None and cart.owner != request.user:
        raise PermissionDenied({"cart_id": ["You must be an owner of the cart to change it"]})

    amount = serializer.validated_data["amount"]
    product = get_object_or_404(Product, pk=serializer.validated_data["product_id"])

    return cart, product, amount


@api_view(["POST"])
def cart_add_product(request) -> Response:
    try:
        cart, product, amount = deserialize_cart_data(request)
    except ValidationError as e:
        return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
    except PermissionDenied as e:
        return Response(e.detail, status=status.HTTP_403_FORBIDDEN)
    
    # check if the product is already in the cart
    if CartEntry.objects.filter(product=product, cart=cart).exists():
        entry = CartEntry.objects.get(product=product, cart=cart)
        if (entry.quantity + amount) > entry.product.quantity:
            return Response({"amount": ["There are not enough items on the stock for given product"]}, status=status.HTTP_400_BAD_REQUEST)
        entry.quantity += amount
        entry.save()
    else:
        entry = CartEntry.objects.create(product=product, quantity=amount, cart=cart)

    return Response(status=status.HTTP_200_OK)


@api_view(["POST"])
def cart_subtract_product(request):
    cart, product, amount = deserialize_cart_data(request)

    # check if the product is already in the cart
    if CartEntry.objects.filter(product=product, cart=cart).exists():
        entry = CartEntry.objects.get(product=product, cart=cart)
        if (entry.quantity - amount) <= 0:
            entry.delete()
        else:
            entry.quantity -= amount
            entry.save()

    return Response(status=status.HTTP_200_OK)
