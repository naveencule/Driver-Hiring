# Generated by Django 4.1.7 on 2023-03-27 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hiring_app', '0005_driver_reg_experience'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver_reg',
            name='district',
        ),
        migrations.RemoveField(
            model_name='driver_reg',
            name='state',
        ),
    ]
