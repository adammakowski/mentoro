# Generated by Django 3.1 on 2020-09-07 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200907_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicprofile',
            name='first_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='publicprofile',
            name='last_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]