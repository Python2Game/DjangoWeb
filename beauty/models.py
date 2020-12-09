from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User_status(models.Model):
    status = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.status

class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    status = models.ForeignKey(User_status,on_delete=models.CASCADE,null=True)
    mobile = models.IntegerField(null=True)
    def __str__(self):
        return self.user.username

class Servise(models.Model):
    name = models.CharField(max_length=100,null=True)
    cost = models.IntegerField(null=True)
    def __str__(self):
        return self.name

class Book_status(models.Model):
    status = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.status

class Apponitment(models.Model):
    service = models.ForeignKey(Servise,on_delete=models.CASCADE,null=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    status = models.ForeignKey(Book_status,on_delete=models.CASCADE,null=True)
    date1 = models.DateField(null=True)
    time1 = models.TimeField(null=True)
    def __str__(self):
        return self.customer.user.username+" "+self.service.name
