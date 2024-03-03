from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.store, name="home_page"),
    path("store/", views.store, name="store"),
    path("store/<uuid:category_id>/", views.store, name="store"),
    path("product/<uuid:product_id>/", views.product, name="product"),
    path("api/", include("shop.api.urls")),
]
