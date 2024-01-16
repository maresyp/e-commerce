from django.shortcuts import redirect, render
from django.contrib import messages
from cart.views import get_shopping_cart
from shop.views import store
from Users.views import userAccount
from .forms import DeliveryAddressForm
from .models import Order, OrderEntry
from cart.models import CartEntry

def order_summary(request):
    user_cart = get_shopping_cart(request)  # Pobieranie koszyka dla zalogowanych i niezalogowanych użytkowników
    cart_items = CartEntry.objects.filter(cart=user_cart) if user_cart else []
    total_price = 0.0

    for item in cart_items:
            item.total_price = item.quantity * item.product.price
            total_price += item.total_price

    if request.method == 'POST':
        form = DeliveryAddressForm(request.POST, user=request.user if request.user.is_authenticated else None)
        if form.is_valid():
            order = form.save(commit=False)
            if request.user.is_authenticated:
                order.owner = request.user
            order.save()

            for item in cart_items:
                OrderEntry.objects.create(order=order, product=item.product, quantity=item.quantity)

            if cart_items:
                cart_items.delete()

            messages.success(request, 'Złożono zamówienie.')
            if request.user.is_authenticated:
                return redirect('userAccount')
            else:
                return redirect('store')
    else:
        form = DeliveryAddressForm(user=request.user if request.user.is_authenticated else None)

    context = {'total_price': total_price, 'form': form, 'cart_items': cart_items,}
    return render(request, 'order/order_summary.html', context)
