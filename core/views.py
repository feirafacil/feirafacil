from django.shortcuts import render
from .forms import ConsumerForm
from .forms import AddressForm
# Create your views here.
def home(request):
    
    return render(request, 'core/home.html', {})

def login(request):
    
    return render(request, 'core/login.html', {})

def signin(request):

    form_consumer = ConsumerForm()
    form_address = AddressForm()
    return render(request, 'core/signin.html', {'form_consumer': form_consumer, 'form_address':form_address})

def about(request):

	return render(request, 'core/about.html', {})