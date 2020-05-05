from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=255)

class Game(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999)
    publisher = models.CharField(max_length=255)
    price = models.IntegerField()
    display = models.BooleanField()
    leftInStock = models.IntegerField()

class GameGenre(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

class GameImage(models.Model):
    image = models.CharField(max_length=999)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

