from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=255)

class User(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    streetname = models.CharField(max_length=255)
    housenumber = models.IntegerField()
    zipcode = models.IntegerField()
    city = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

class phoneNr(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phoneNr = models.IntegerField()