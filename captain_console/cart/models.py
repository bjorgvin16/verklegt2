from django.db import models
from userprofile.models import User
from frontpage.models import Product

class Cart(models.Model):
    customerId = models.ForeignKey(User, on_delete=models.CASCADE)
    inuse = models.BooleanField()

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()