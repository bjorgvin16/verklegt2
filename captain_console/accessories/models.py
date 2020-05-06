from django.db import models
from frontpage.models import Product

class Accessory(Product):
    pass

    def __str__(self):
        return self.name