from django.shortcuts import render

from django.contrib.auth.models import User
from django.shortcuts import redirect
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def do_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'core/consumer.html')
            else:
                return render(request, 'core/login.html' )
        else:
            return render(request, 'core/login.html' )
    else:
        form = LoginForm()
        islogged = is_logged(request)
        return render(request, 'core/login.html', {'form': form, 'is_logged': islogged})

def home(request):
    islogged = is_logged(request)
    return render(request, 'core/home.html', {'is_logged': islogged})

def signin_django(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('core.views.home')
    else:
        form = UserForm()
        return render(request, 'core/signin_django.html', {'form': form, 'is_logged': True})

def signin(request):
    if request.method == "POST":
        form = ConsumerForm(request.POST)
        if form.is_valid():
            consumer = form.save(commit=False)
            user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
            consumer.user = user
            consumer.save()
            return redirect('core.views.home')
    else:
        form = ConsumerForm()
        return render(request, 'core/signin.html', {'form': form, 'is_logged': True})

def merchant_signin(request):
    if request.method == "POST":
        form = MerchantForm(request.POST)
        if form.is_valid():
            merchant = form.save(commit=False)
            user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
            merchant.user = user
            merchant.save()
            return redirect('core.views.home')
    else:
        form = MerchantForm()
        return render(request, 'core/signin.html', {'form': form, 'is_logged': True})

def about(request):

	return render(request, 'core/about.html', {'is_logged': True})

@login_required
def consumer(request):

	return render(request, 'core/consumer.html', {'is_logged': True})

@login_required
def merchant(request):

	return render(request, 'core/merchant.html', {'is_logged': True})

@login_required
def list(request):
    if request.method == "POST":
        form = ListProductForm(request.POST)
        if form.is_valid():
            list_product = form.save(commit=False)
            list_product.save()
            return redirect('core.views.consumer')
    else:
        form = ListProductForm()
        return render(request, 'core/list.html', {'form': form, 'is_logged': True})

@login_required
def product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect('core.views.list')
    else:
        form = ProductForm()
        return render(request, 'core/product.html', {'form': form, 'is_logged': True})

@login_required
def tender(request):
    if request.method == "POST":
        form = TenderForm(request.POST)
        if form.is_valid():
            tender = form.save(commit=False)
            tender.save()
            return redirect('core.views.merchant')
    else:
        form = TenderForm()
        return render(request, 'core/tender.html', {'form': form, 'is_logged': True})

@login_required
def notification(request):
    return render(request, 'core/notification.html', {})

def is_logged(request):
    current_user = request.user
    if(current_user.id == None):
        return True
    else:
        return False
