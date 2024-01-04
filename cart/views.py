import datetime

from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.contrib import messages

from shop.models import Product

from .models import CartEntry, ShoppingCart


# Create your views here.
def cart(request):
    # check if request comes from logged in user
    user_cart = get_or_create_shopping_cart(request)

    entries = CartEntry.objects.filter(
        Q(cart=user_cart),
    )
    total = 0.0

    if entries:
        for entry in entries:
            entry.total_price = entry.quantity * entry.product.price
            total += entry.total_price

    context = {'entries': entries, 'total_price': total}

    return render(request, 'cart/cart.html', context)

def add_product_to_cart(request, product_id, quantity: int):
    product = get_object_or_404(Product, pk=product_id)
    user_cart = get_or_create_shopping_cart(request)

    # check if the product is already in the cart
    if CartEntry.objects.filter(product=product, cart=user_cart).exists():
        entry = CartEntry.objects.get(product=product, cart=user_cart)
        entry.quantity += quantity
        entry.save()
    else:
        entry = CartEntry.objects.create(product=product, quantity=quantity, cart=user_cart)
        entry.save()

    messages.success(request, 'Product added to cart')
    return redirect('home_page')

def delete_product_from_cart(request, entry_id):
    cart = get_shopping_cart(request)

    if cart is None:
        messages.error(request, 'Cart not found')
        return redirect('cart')

    if cart.owner is not None and cart.owner != request.user:
        messages.error(request, 'You are not allowed to delete this product')
        return redirect('cart')

    entry = CartEntry.objects.get(pk=entry_id)

    if entry is None:
        messages.error(request, 'Entry not found')
        return redirect('cart')

    if entry.cart != cart:
        messages.error(request, 'You are not allowed to delete this product')
        return redirect('cart')

    entry.delete()

    messages.success(request, 'Product deleted from cart')
    return redirect('cart')

def get_or_create_shopping_cart(request) -> ShoppingCart:
    user_cart = None
    if request.user.is_authenticated:
        user = request.user
        user_cart, created = ShoppingCart.objects.get_or_create(owner=user)
    else:
        # Get the session of the user
        user_session = request.session
        if 'cart_id' in user_session:
            cart_id = user_session['cart_id']
            user_cart = ShoppingCart.objects.get(pk=cart_id)
        else:
            user_cart = ShoppingCart.objects.create(expiration_date=timezone.now() + datetime.timedelta(days=14))
            user_session['cart_id'] = str(user_cart.id)

    if user_cart is None:
        raise Exception('Cart not found')


    messages.success(request, 'Produkt dodany do koszyka!')

    return redirect(request.META.get('HTTP_REFERER')

def get_shopping_cart(request) -> ShoppingCart | None:
    user_cart = None
    if request.user.is_authenticated:
        user = request.user
        user_cart = ShoppingCart.objects.get(owner=user)
    else:
        # Get the session of the user
        user_session = request.session
        if 'cart_id' in user_session:
            cart_id = user_session['cart_id']
            user_cart = ShoppingCart.objects.get(pk=cart_id)

    return user_cart