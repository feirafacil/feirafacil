from django.db import models
from django.db.models.signals import post_save
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

    def __str__(self):
        return self.name

class Merchant(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=9)
    phone = models.CharField(max_length=10)
    zone = models.ForeignKey('Zone')

    def __str__(self):
        return self.username

class Zone(models.Model):
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description

class ListProduct(models.Model):
    consumer = models.ForeignKey('Consumer')
    products = models.ManyToManyField('Product')

class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.name

class MerchantTender(models.Model):
    merchant = models.ForeignKey('Merchant')
    list_product = models.ForeignKey('ListProduct')
    price = models.FloatField()

class ConsumerNotification(models.Model):
    consumer = models.ForeignKey('Consumer')
    message = models.TextField()

class MerchantNotification(models.Model):
    merchant = models.ForeignKey('Merchant')
    message = models.TextField()

def notify_merchant(sender, **kwargs):
    if kwargs['created']:
        print ("função de notificação do comerciante")
        list_product = kwargs['instance']
        print (list_product.consumer.name)
        print (list_product.consumer.address)

post_save.connect(notify_merchant, sender=ListProduct)

def notify_consumer(sender, **kwargs):
    if kwargs['created']:
        print ("função de notificação do cosumidor")
        merchant_tender = kwargs['instance']
        print (merchant_tender.list_product.consumer.name)
        print (merchant_tender.list_product.consumer.address)

post_save.connect(notify_consumer, sender=MerchantTender)