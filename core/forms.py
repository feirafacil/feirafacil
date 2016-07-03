from django import forms
from .models import Consumer
from .models import Product
from .models import ListProduct
from .models import MerchantTender
from django.contrib.auth.models import User

class ConsumerForm(forms.ModelForm):
    
    class Meta:
        model = Consumer
        fields = ('name', 'email', 'password', 'phone','city', 'address', 'cep', 'number')

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ('name', 'description')

class ListProductForm(forms.ModelForm):
    
    class Meta:
        model = ListProduct
        fields = ('consumer', 'products')

class TenderForm(forms.ModelForm):
    
    class Meta:
        model = MerchantTender
        fields = ('merchant', 'list_product', 'price')

class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('username', 'password', 'email')

class LoginForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('username', 'password')
