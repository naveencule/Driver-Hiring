# Generated by Django 4.1.7 on 2023-03-27 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hiring_app', '0004_driver_reg_con_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver_reg',
            name='experience',
            field=models.CharField(max_length=100, null=True),
        ),
    ]