from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Appointment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100,null=True)
    contact = models.CharField(max_length=100,null=True)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True,null=True)
    reason = models.CharField(max_length=100,null=True)
    slot = models.CharField(max_length=100,null=True)

class AppointmentHistory(models.Model):
    user = models.IntegerField(null=True)
    name = models.CharField(max_length=100,null=True)
    contact = models.CharField(max_length=100,null=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    reason = models.CharField(max_length=100,null=True)
    slot = models.CharField(max_length=100,null=True)
    doct_notes =  models.CharField(max_length=100,null=True)

class Slots(models.Model):
    slot = models.CharField(max_length=40)
