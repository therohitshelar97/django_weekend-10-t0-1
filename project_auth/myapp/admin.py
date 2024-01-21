from django.contrib import admin
from .models import Appointment

# Register your models here.
@admin.register(Appointment)
class AdminApp(admin.ModelAdmin):
    list_display = ['name','contact','date','reason']