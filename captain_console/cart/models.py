from django.db import models
from django.contrib.auth.models import User

from users.models import Profile
from frontpage.models import Product


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    num = models.IntegerField()

    #def get_cart_items(self):
    #    return self.items.all()

    #def get_cart_total(self):
    #    return sum([item.product.price for item in self.items.all()])



