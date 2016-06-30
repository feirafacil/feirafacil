from django.shortcuts import render

# Create your views here.
def home(request):
    
    return render(request, 'core/home.html', {})

def login(request):
    
    return render(request, 'core/login.html', {})

def signin(request):

	return render(request, 'core/signin.html', {})

def about(request):

	return render(request, 'core/about.html', {})