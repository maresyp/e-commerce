from django.urls import path

from . import views

urlpatterns = [
    path('', views.store, name="home_page"),
    path('store/', views.store, name='store'),
    path('store/<uuid:category_id>/', views.store, name='store'),
]
