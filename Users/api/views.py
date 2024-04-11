from __future__ import annotations

from uuid import UUID

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from cart.models import ShoppingCart

from .serializers import NewUserSerializer


@api_view(["GET"])
def get_routes(_request):
    routes = [
        "/api/token",
        "/api/token/refresh",
    ]

    return Response(routes)


@api_view(["POST"])
def register_user(request) -> Response:
    user_serializer = NewUserSerializer(data=request.data)

    if not user_serializer.is_valid():
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(email=user_serializer.data["email"]).exists():
        return Response({"errors": ["User with this email address already exists."]}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(
        username=user_serializer.data["email"],
        email=user_serializer.data["email"],
        password=user_serializer.data["password"],
        first_name=user_serializer.data["first_name"],
    )

    if user_serializer.data["cart_id"]:
        cart = get_object_or_404(ShoppingCart, pk=UUID(user_serializer.data["cart_id"]))
        if cart.owner is not None:
            return Response({"errors": ["This cart is already owned by someone."]}, status=status.HTTP_400_BAD_REQUEST)

        cart.owner = user
        cart.save()

    return Response(status=status.HTTP_201_CREATED)
