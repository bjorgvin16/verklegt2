from django.db import models

from frontpage.models import Product
from consoles.models import Console
# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=255)

class Game(Product):
    releaseYear = models.IntegerField()
    gameConsole = models.ForeignKey(Console, on_delete=models.CASCADE)

class GameGenre(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)


