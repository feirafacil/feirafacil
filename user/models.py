from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=9)
    phone = models.CharField(max_length=10)

class Consumer(User):
    address = models.ForeignKey('Address')


class Merchant(User):
    zone = models.ForeignKey('Zone')
    
class Address(models.Model):
    description = models.CharField(max_length=200)
    number = models.CharField(max_length=2)
    cep = models.CharField(max_length=9)

class Zone(models.Model):
    description = models.CharField(max_length=200)