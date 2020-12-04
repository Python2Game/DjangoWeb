from django.db import models

class Register(models.Model):
    title = models.CharField('Название услуги', max_length=40)
    name = models.CharField('Ваше имя', max_length=20)
full_text = models.TextField('Блабла')
date= models.DateTimeField('Дата')
