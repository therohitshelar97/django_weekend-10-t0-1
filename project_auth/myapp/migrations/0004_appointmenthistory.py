# Generated by Django 5.0.1 on 2024-02-04 06:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_slots_appointment_slot'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('contact', models.CharField(max_length=100, null=True)),
                ('date', models.DateField(auto_now=True)),
                ('time', models.TimeField(auto_now=True, null=True)),
                ('reason', models.CharField(max_length=100, null=True)),
                ('slot', models.CharField(max_length=100, null=True)),
                ('doct_notes', models.CharField(max_length=100, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]