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

    def get_add_to_cart_url(self):
        return reverse("cart:add-to-cart", kwargs={
            'item_id': self.id
        })

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    image = models.CharField(max_length=999)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.image + " ------ " + self.product.name