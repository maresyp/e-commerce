from django.urls import path

from . import views

urlpatterns = [
    path("get_all_products/", views.get_all_products),
    path("get_product_image/<uuid:product_id>", views.get_product_image),
    path("get_products_with_category/<str:category>", views.get_products_with_category),
    path("get_single_product/<uuid:product_id>", views.get_single_product),
    path("get_all_categories/", views.get_all_categories),
]
