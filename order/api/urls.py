from django.urls import path

from . import views

urlpatterns = [
    path("create_order/", views.create_order),
    path("order_history/", views.order_history),
]
