from django.shortcuts import render

from .models import Product

# Create your views here.

def store(request):
    page = 'store'
    products = Product.objects.all()
    context = {'products': products, 'page': page}

    return render(request, 'shop/store.html', context)

