# Generated by Django 4.2.5 on 2023-12-10 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_adharcard_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adharcard',
            name='adhar_no',
            field=models.BigIntegerField(null=True, unique=True),
        ),
    ]
