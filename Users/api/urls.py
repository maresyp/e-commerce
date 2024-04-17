from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views

urlpatterns = [
    path("", views.get_routes),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", views.register_user, name="register_user"),
    path("change_password/", views.change_password, name="change_password"),
    path("update_profile/", views.update_profile, name="update_profile"),
]
