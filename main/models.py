from django.db import models
from django.contrib.auth.models import User

class MyUser(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    senha = models.CharField(max_length=9)
    telefone = models.CharField(max_length=10)

class Consumer(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    senha = models.CharField(max_length=30)
    telefone = models.CharField(max_length=10)
    cidade= models.CharField(max_length=50)
    logradouro = models.CharField(max_length=200)
    numero = models.CharField(max_length=2)
    cep = models.CharField(max_length=9)
    def save(self, *args, **kwargs):
        consumer = super(Consumer, self).save(*args, **kwargs)
        User.objects.create_user('test', 'test@gmail.com', "testpass")
        

class Merchant(MyUser):
    zone = models.ForeignKey('Zone')
    
class Address(models.Model):
    cidade= models.CharField(max_length=50)
    logradouro = models.CharField(max_length=200)
    numero = models.CharField(max_length=2)
    cep = models.CharField(max_length=9)

class Zone(models.Model):
    description = models.CharField(max_length=200)