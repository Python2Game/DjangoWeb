from django.db import models

class Task(models.Model):
    name = models.CharField('Ваше имя', max_length=20)
    title = models.CharField('Название услуги', max_length=40)



    def __str__(self):
        return self.name
