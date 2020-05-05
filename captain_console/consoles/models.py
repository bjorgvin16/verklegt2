from django.db import models

# Create your models here.
class Consoles(models.Model):
    name = models.CharField(max_length=255)
    descirption = models.CharField(max_length=999)
    manufacturer = models.CharField(max_length=999)
    price = models.IntegerField()
    display = models.BooleanField()
    leftInStock = models.IntegerField()

class ConsoleImage(models.Model):
    image = models.CharField(max_length=999)
    game = models.ForeignKey(Consoles, on_delete=models.CASCADE)