from django.db import models

class User(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

class phoneNr(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phoneNr = models.IntegerField()

class UserImage(models.Model):
    image = models.CharField(max_length=999)
    user = models.ForeignKey(User, on_delete=models.CASCADE)