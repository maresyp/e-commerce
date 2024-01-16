import uuid

from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    STATUS_CHOICES = [
        ('1', 'Złożone'),
        ('2', 'W trakcie przygotowania'),
        ('3', 'Wysłane'),
        ('4', 'Dostarczone'),
    ]

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    date_of_order = models.DateTimeField(null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    street = models.CharField(max_length=255, null=True, blank=True)
    house_number = models.CharField(max_length=255, null=True, blank=True)
    postal_code = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=40, null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='1')

    def __str__(self):
        return f'Order {self.id} owned by {self.owner}'


class OrderEntry(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product = models.ForeignKey('shop.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f'Entry {self.id} with {self.quantity} {self.product} from order {self.oreder.id}'