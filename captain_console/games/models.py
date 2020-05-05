from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.Charfield(max_length=255)
    description = models.CharField(max_length=999)