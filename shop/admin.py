from django.contrib import admin

from .models import Product, MainCategory, SubCategory

# Register your models here.
admin.site.register(Product)
admin.site.register(MainCategory)
admin.site.register(SubCategory)
