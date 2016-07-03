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
    
    return render(request, 'main/home.html', {})

def signin(request):
    if request.method == "POST":
        form = ConsumerForm(request.POST)
        if form.is_valid():
            consumer = form.save(commit=False)
            print (consumer.nome)
            consumer.save()
            return redirect('main.views.home')
    else:
        form_consumer = ConsumerForm()
        return render(request, 'main/signin.html', {'form_consumer': form_consumer})

def about(request):

	return render(request, 'main/about.html', {})

def consumer(request):

	return render(request, 'main/consumer.html', {})

def merchant(request):

	return render(request, 'main/merchant.html', {})

def list(request):
    if request.method == "POST":
        form = ListProductForm(request.POST)
        if form.is_valid():
            list_product = form.save(commit=False)
            list_product.save()
            return redirect('main.views.consumer')
    else:
        form = ListProductForm()
        return render(request, 'main/list.html', {'form': form})

def product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect('main.views.list')
    else:
        form = ProductForm()
        return render(request, 'main/product.html', {'form': form})

def tender(request):
    if request.method == "POST":
        form = TenderForm(request.POST)
        if form.is_valid():
            tender = form.save(commit=False)
            tender.save()
            return redirect('main.views.list')
    else:
        form = ProductForm()
        return render(request, 'main/tender.html', {'form': form})
