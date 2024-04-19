from __future__ import annotations

from uuid import UUID

from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from cart.models import ShoppingCart
from Users.models import Profile

from .serializers import ChangePasswordSerializer, NewUserSerializer, ProfileSerializer


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

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def change_password(request):
    deserializer = ChangePasswordSerializer(data=request.data)
    if not deserializer.is_valid():
        return Response(deserializer.errors, status=status.HTTP_400_BAD_REQUEST)

    user = request.user

    if not check_password(deserializer.validated_data["old_password"], user.password):
        return Response({"error": "Stare hasło jest niepoprawne"}, status=status.HTTP_400_BAD_REQUEST)

    user.password = make_password(deserializer.validated_data["user.password"])
    user.save()

    return Response(status=status.HTTP_200_OK)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def update_profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)

    serializer = ProfileSerializer(instance=profile, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)

    serializer = ProfileSerializer(profile)

    return Response(data=serializer.data, status=status.HTTP_200_OK)
