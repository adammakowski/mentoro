# Generated by Django 3.1 on 2020-08-08 21:06

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200808_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=ckeditor.fields.RichTextField(help_text='Napisz szczegółowy komentarz. Wesprzyj Twórcę tego postu i przekaż swoje podziękowania lub uwagi.', verbose_name='Treść komentarza'),
        ),
    ]
