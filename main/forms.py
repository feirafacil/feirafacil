from django import forms
from .models import Consumer
from .models import Product
from .models import ListProduct

class ConsumerForm(forms.ModelForm):
    
    class Meta:
        model = Consumer
        fields = ('nome', 'email', 'senha', 'telefone','cidade', 'logradouro', 'cep', 'numero')

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ('name', 'description')

class ListProductForm(forms.ModelForm):
    
    class Meta:
        model = ListProduct
        fields = ('consumer', 'products')