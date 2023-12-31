# Generated by Django 4.2.5 on 2023-12-10 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_adharcard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adharcard',
            name='adhar_no',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='adharcard',
            name='person',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.person'),
        ),
    ]
