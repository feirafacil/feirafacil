from django import forms
from .models import Consumer
from .models import Address

class ConsumerForm(forms.ModelForm):
    
    class Meta:
        model = Consumer
        fields = ('nome', 'email', 'senha', 'telefone',)

class AddressForm(forms.ModelForm):
    
    class Meta:
        model = Address
        fields = ('cep', 'cidade', 'logradouro', 'numero', )
