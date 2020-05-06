from django.db import models

from frontpage.models import Product

# Create your models here.
class Console(Product):
    pass

    def __str__(self):
        return self.name