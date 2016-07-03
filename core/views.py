from django.shortcuts import render

from django.shortcuts import render
from django.shortcuts import redirect
from .forms import *
from django.contrib.auth import authenticate, login

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
        else:
            # Return a 'disabled account' error message
            ...
    else:
        # Return an 'invalid login' error message.
        ...
def home(request):
    
    return render(request, 'core/home.html', {})

def signin(request):
    if request.method == "POST":
        form = ConsumerForm(request.POST)
        if form.is_valid():
            consumer = form.save(commit=False)
            consumer.save()
            return redirect('core.views.home')
    else:
        form_consumer = ConsumerForm()
        return render(request, 'core/signin.html', {'form_consumer': form_consumer})

def about(request):

	return render(request, 'core/about.html', {})

def consumer(request):

	return render(request, 'core/consumer.html', {})

def merchant(request):

	return render(request, 'core/merchant.html', {})

def list(request):
    if request.method == "POST":
        form = ListProductForm(request.POST)
        if form.is_valid():
            list_product = form.save(commit=False)
            list_product.save()
            return redirect('core.views.consumer')
    else:
        form = ListProductForm()
        return render(request, 'core/list.html', {'form': form})

def product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect('core.views.list')
    else:
        form = ProductForm()
        return render(request, 'core/product.html', {'form': form})

def tender(request):
    if request.method == "POST":
        form = TenderForm(request.POST)
        if form.is_valid():
            tender = form.save(commit=False)
            tender.save()
            return redirect('core.views.list')
    else:
        form = ProductForm()
        return render(request, 'core/tender.html', {'form': form})
