from django.db import models

class User(models.Model):
<<<<<<< HEAD
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
=======
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
>>>>>>> 986cf2ca09dfb8187ded6f0067c6688ed5d8ab2c

class phoneNr(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phoneNr = models.IntegerField()

class UserImage(models.Model):
    image = models.CharField(max_length=999)
    user = models.ForeignKey(User, on_delete=models.CASCADE)