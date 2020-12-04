from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('makeup', views.makeup),
    path('manicure', views.manicure),
    path('register', views.register),
    path('check', views.check),
    
]