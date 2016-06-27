from django import forms
from .models import Consumer

class ConsumerForm(forms.ModelForm):
    
    class Meta:
        model = Consumer
        fiels = ('nome', 'email', 'password', 'phone', 'address')