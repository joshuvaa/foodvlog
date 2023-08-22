# from ..shop.models import Products
from django.db import models
from shop.models import Products


# Create your models here.

class Cartlist(models.Model):
    cart_id = models.CharField(max_length=250, unique=True)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cart_id


class item(models.Model):
    prodt = models.ForeignKey(Products, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cartlist, on_delete=models.CASCADE)
    quan = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.prodt

    def total(self):
        return self.prodt.price * self.quan
