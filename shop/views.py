from django.shortcuts import render

from .models import Product, MainCategory


# Create your views here.

def store(request, category_id=None):
    page = 'store'
    categories = MainCategory.objects.all()
    
    if category_id:
        products = Product.objects.filter(category__mainCategory__id=category_id)
    else:
        products = Product.objects.all()
    context = {'products': products, 'page': page, 'categories': categories}

    return render(request, 'shop/store.html', context)

