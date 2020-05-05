from django.db import models
# it's not perfect but it's something

class Cart(models.Model):
    totalPrice = models.IntegerField()
    itemNum = models.IntegerField()
    customerId = models.ForeignKey(userprofile, on_delete=models.CASCADE) #NEED TO MAKE THIS TABLE

