from django.shortcuts import get_object_or_404, render
from .models import MainCategory, SubCategory, Product

def store(request, category_id=None):
    page = 'store'
    categories = MainCategory.objects.all()
    subcategories = SubCategory.objects.none()

    # Filtrowanie produktów na podstawie kategorii głównej
    if category_id:
        products = Product.objects.filter(category__mainCategory__id=category_id)
        subcategories = SubCategory.objects.filter(mainCategory__id=category_id).distinct()
    else:
        products = Product.objects.all()
        subcategories = SubCategory.objects.all().distinct()

    # Filtrowanie na podstawie zapytania wyszukiwania
    query = request.GET.get('q')
    if query:
        products = products.filter(name__icontains=query)

    # Filtrowanie na podstawie wybranych podkategorii
    selected_subcategories = request.GET.getlist('subcat')
    if selected_subcategories:
        products = products.filter(category__id__in=selected_subcategories)

    # Grupowanie podkategorii według głównych kategorii
    category_subcategories = {}
    for category in categories:
        category_subcategories[category] = SubCategory.objects.filter(mainCategory=category).distinct()

    context = {
        'products': products,
        'page': page,
        'categories': categories,
        'category_subcategories': category_subcategories,
        'selected_subcategories': selected_subcategories,  # Dodano
        'category_id': category_id
    }

    return render(request, 'shop/store.html', context)

def product(request, product_id):
    page = 'product_details'
    product = get_object_or_404(Product, id=product_id)

    context = {
        'page': page,
        'product': product,
    }
    return render(request, 'shop/product.html', context)