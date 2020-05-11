from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from frontpage.models import Product
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

def post_save_profile_create(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)

post_save.connect(post_save_profile_create, sender=settings.AUTH_USER_MODEL)