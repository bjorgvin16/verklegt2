from django.db import models

from consoles.models import Consoles
# Create your models here.

class Genres(models.Model):
    name = models.CharField(max_length=255)

class Games(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999)
    publisher = models.CharField(max_length=255)
    price = models.IntegerField()
    display = models.BooleanField()
    leftInStock = models.IntegerField()
    console = models.ForeignKey(Consoles, on_delete=models.CASCADE)

class GameGenre(models.Model):
    game = models.ForeignKey(Games, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE)

class GameImage(models.Model):
    image = models.CharField(max_length=999)
    game = models.ForeignKey(Games, on_delete=models.CASCADE)

