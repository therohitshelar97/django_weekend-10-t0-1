from django.db import models

# Create your models here.

class Appointment(models.Model):
    name = models.CharField(max_length=100,null=True)
    contact = models.CharField(max_length=100,null=True)
    date = models.DateField(auto_now=True)
    reason = models.CharField(max_length=100,null=True)
