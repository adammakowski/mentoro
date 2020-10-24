# Generated by Django 3.1.2 on 2020-10-24 09:41

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20201024_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='public',
            name='bio',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Biografia'),
        ),
        migrations.AlterField(
            model_name='public',
            name='first_name',
            field=models.CharField(default='', max_length=100, verbose_name='Imię'),
        ),
        migrations.AlterField(
            model_name='public',
            name='last_name',
            field=models.CharField(default='', max_length=100, verbose_name='Nazwisko'),
        ),
    ]