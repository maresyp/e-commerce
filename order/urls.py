from django.urls import include, path

from . import views

urlpatterns = [
    path("order_summary/", views.order_summary, name="order_summary"),
    path("api/", include("order.api.urls")),
]
