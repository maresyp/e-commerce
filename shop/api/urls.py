from django.urls import path

from . import views

urlpatterns = [
    path("get_all_products/", views.get_all_products),
    path("get_product_image/<uuid:product_id>", views.get_product_image),
]
