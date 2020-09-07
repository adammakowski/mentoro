# Generated by Django 3.1 on 2020-08-06 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200806_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(default='', max_length=150, unique=True),
        ),
        migrations.AddField(
            model_name='historicalblogpost',
            name='slug',
            field=models.SlugField(default='', max_length=150),
        ),
    ]