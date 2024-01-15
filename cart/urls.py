from django.urls import path

from . import views

urlpatterns = [
    path('cart/', views.cart, name="cart"),
    path('add_product_to_cart/<uuid:product_id>/<int:quantity>/', views.add_product_to_cart, name="add_product_to_cart"),
    path('delete_product_from_cart/<uuid:entry_id>/', views.delete_product_from_cart, name="delete_product_from_cart"),
    path('cart/increase/<uuid:entry_id>/', views.increase_product_quantity, name='increase_product_quantity'),
    path('cart/decrease/<uuid:entry_id>/', views.decrease_product_quantity, name='decrease_product_quantity'),
]
