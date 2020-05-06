from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    price = models.IntegerField()
    display = models.BooleanField()
    leftInStock = models.IntegerField()
    image = models.CharField(max_length=999)

    def __str__(self):
        return self.name