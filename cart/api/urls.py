from django.urls import path

from . import views

urlpatterns = [
    path("cart_get/", views.get_shopping_cart),
    path("cart_add_product/", views.cart_add_product),
    path("cart_remove_product/", views.cart_remove_product),
]
