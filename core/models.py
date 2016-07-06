from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Consumer(models.Model):
    username = models.CharField(max_length=30)
    user = models.ForeignKey(User)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    number = models.CharField(max_length=2)
    cep = models.CharField(max_length=9)

    def __str__(self):
        return self.username

class Merchant(models.Model):
    username = models.CharField(max_length=200)
    user = models.ForeignKey(User)
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
        list_product = kwargs['instance']
        merchants = Merchant.objects.all()
        for merchant in merchants:
            notification = MerchantNotification()
            notification.merchant = merchant
            notification.message = 'Nova lista disponivel na sua zona'
            notification.save()


post_save.connect(notify_merchant, sender=ListProduct)

def notify_consumer(sender, **kwargs):
    if kwargs['created']:
        merchant_tender = kwargs['instance']
        notification = ConsumerNotification()
        notification.consumer = merchant_tender.list_product.consumer
        notification.message = 'Nova oferta na sua lista'
        notification.save()

post_save.connect(notify_consumer, sender=MerchantTender)