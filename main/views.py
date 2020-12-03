from django.shortcuts import render

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


