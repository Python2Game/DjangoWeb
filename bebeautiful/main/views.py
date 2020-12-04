from django.shortcuts import render
from .forms import RegisterForm
from .models import Register

def check(request):
    return render(request, 'main/main/check.html')

def index(request):
    return render(request, 'main/index.html')

def makeup(request):
    return render(request, 'main/makeup.html')

def manicure(request):
    return render(request, 'main/manicure.html')

def register(request):
    return render(request, 'main/register.html')

def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')

def go(request):
    return render(request, 'main/go.html')    

def data(request):

    form = RegisterForm()
    date ={'form': form}

    return render(request, 'main/data.html')


