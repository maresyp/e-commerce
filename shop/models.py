import uuid

from django.db import models

# Create your models here.

class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.name
