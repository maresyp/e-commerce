from django.contrib import admin

from .models import Order,OrderEntry
# Register your models here.
admin.site.register(Order)
admin.site.register(OrderEntry)