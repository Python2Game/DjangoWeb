from django.db import models
from django.forms import ModelForm, TextInput, DateTimeInput,Textarea

class Register(models.Model):
    title = models.CharField('Название услуги', max_length=40)
    name = models.CharField('Ваше имя', max_length=20)
    date= models.DateTimeField('Дата')
    time = models.TextField('Время')
