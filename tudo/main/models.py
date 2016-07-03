from django.db import models
from django.contrib.auth.models import User


class Consumer(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    number = models.CharField(max_length=2)
    cep = models.CharField(max_length=9)
    '''def save(self, *args, **kwargs):
        consumer = super(Consumer, self).save(*args, **kwargs)
        User.objects.create_user('test', 'test@gmail.com', "testpass")'''

class Merchant(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=9)
    phone = models.CharField(max_length=10)
    zone = models.ForeignKey('Zone')

class Zone(models.Model):
    description = models.CharField(max_length=200)

class ListProduct(models.Model):
    consumer = models.ForeignKey('Consumer')
    products = models.ManyToManyField('Product')

class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()

class Tender(models.Model):
    merchant = models.ForeignKey('Merchant')
    list_product = models.ForeignKey('ListProduct')
    price = models.FloatField()
