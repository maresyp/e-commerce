import datetime

from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from shop.models import Product

from .models import CartEntry, ShoppingCart


# Create your views here.
def cart(request):
    # check if request comes from logged in user
    user_cart = None
    if request.user.is_authenticated:
        user = request.user
        user_cart, created = ShoppingCart.objects.get_or_create(owner=user)
    else:
        # Get the session of the user
        user_session = request.session
        if 'cart_id' in user_session:
            cart_id = user_session['cart_id']
            user_cart = ShoppingCart.objects.get_or_create(pk=cart_id)

    entries = CartEntry.objects.filter(
        Q(cart=user_cart),
    )

    context = {'entries': entries}

    return render(request, 'cart/cart.html', context)

def add_product(request, product_id, quantity: int):
    product = get_object_or_404(Product, pk=product_id)


    # check if request comes from logged in user
    if request.user.is_authenticated:
        user = request.user
        user_cart, created = ShoppingCart.objects.get_or_create(owner=user)

        # check if the product is already in the cart
        if CartEntry.objects.filter(product=product, cart=user_cart).exists():
            entry = CartEntry.objects.get(product=product, cart=user_cart)
            entry.quantity += quantity
            entry.save()
        else:
            entry = CartEntry.objects.create(product=product, quantity=quantity, cart=user_cart)
            entry.save()

    # TODO:<maresyp> Remove code duplication
    else:
        # if the user is not logged in, create new Shopping Cart and save it in the session
        # Get the session of the user
        user_session = request.session

        # Access session data
        if 'cart_id' in user_session:
            cart_id = user_session['cart_id']
            user_cart = ShoppingCart.objects.get(pk=cart_id)
        else:
            # carts for not logged in users are valid for 14 days
            user_cart = ShoppingCart.objects.create(expiration_date=timezone.now() + datetime.timedelta(days=14))
            user_session['cart_id'] = str(user_cart.id)

        # check if the product is already in the cart
        if CartEntry.objects.filter(product=product, cart=user_cart).exists():
            entry = CartEntry.objects.get(product=product, cart=user_cart)
            entry.quantity += quantity
            entry.save()
        else:
            entry = CartEntry.objects.create(product=product, quantity=quantity, cart=user_cart)
            entry.save()

    return redirect('home_page')
