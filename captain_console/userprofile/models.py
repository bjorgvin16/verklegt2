from django.db import models

class User(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

class phoneNr(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phoneNr = models.IntegerField()