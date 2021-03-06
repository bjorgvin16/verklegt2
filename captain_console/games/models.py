from django.db import models

from frontpage.models import Product
from consoles.models import Console

class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Game(Product):
    releaseYear = models.IntegerField()
    gameConsole = models.ForeignKey(Console, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)