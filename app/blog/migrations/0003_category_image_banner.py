# Generated by Django 3.1.2 on 2020-10-22 09:26

from django.db import migrations
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201022_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image_banner',
            field=pyuploadcare.dj.models.ImageField(default='', help_text='Baner kategorii', verbose_name='Baner kategori'),
        ),
    ]