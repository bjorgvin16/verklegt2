from django.db import models
from userprofile.models import User
# it's not perfect but it's something

class Cart(models.Model):
    totalPrice = models.IntegerField()
    itemNum = models.IntegerField()
    customerId = models.ForeignKey(User, on_delete=models.CASCADE)

