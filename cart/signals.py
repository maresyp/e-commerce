import datetime

from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from .models import ShoppingCart

last_clear = datetime.now()

@receiver(post_save, sender=ShoppingCart())
def delete_old_shopping_carts(sender, instance, created, **kwargs):

    global last_clear # noqa: PLW0602
    # if last clear was more than 1 day ago
    if (datetime.now() - last_clear).days >= 1:
        # get all carts without owners
        carts = ShoppingCart.objects.filter(owner=None)
        for cart in carts:
            if cart.expiration_date < datetime.now():
                cart.delete()

