from django.shortcuts import render
from .forms import ConsumerForm
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

    form_consumer = ConsumerForm()
    return render(request, 'main/signin.html', {'form_consumer': form_consumer})

def about(request):

	return render(request, 'main/about.html', {})