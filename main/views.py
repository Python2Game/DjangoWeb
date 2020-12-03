from django.shortcuts import render

def check(request):
    return render(request, 'main/main/check.html')

def index(request):
    return render(request, 'main/index.html')
