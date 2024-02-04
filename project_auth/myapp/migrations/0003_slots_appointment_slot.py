# Generated by Django 4.2.3 on 2024-01-28 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_appointment_time_appointment_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='slot',
            field=models.CharField(max_length=100, null=True),
        ),
    ]