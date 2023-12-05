from django.contrib import admin

from .models import CartEntry, ShoppingCart

# Register your models here.
admin.site.register(ShoppingCart)
admin.site.register(CartEntry)
