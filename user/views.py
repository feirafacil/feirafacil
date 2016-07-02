from django.shortcuts import render
from .forms import ConsumerForm

# Create your views here.
def login(request):
    
    return render(request, 'user/login.html', {})

def singin(request):

    form = ConsumerForm()
    return render(request, 'user/singin.html', {'form': form})