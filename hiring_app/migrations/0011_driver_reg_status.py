# Generated by Django 4.1.7 on 2023-03-28 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hiring_app', '0010_trips'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver_reg',
            name='status',
            field=models.CharField(max_length=100, null=True),
        ),
    ]