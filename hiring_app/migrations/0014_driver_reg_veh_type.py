# Generated by Django 4.1.7 on 2023-04-04 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hiring_app', '0013_delete_vehicle_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver_reg',
            name='veh_type',
            field=models.CharField(max_length=100, null=True),
        ),
    ]