from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('makeup', views.makeup),
    path('manicure', views.manicure),
    path('register', views.register),
    path('check', views.check),
    path('data', views.data),
    path('about', views.about),
    path('contacts', views.contacts),
    path('go', views.go)



    
]