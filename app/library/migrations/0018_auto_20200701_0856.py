# Generated by Django 3.0.7 on 2020-07-01 08:56

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0017_auto_20200701_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicallibraryfile',
            name='requirements',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='libraryfile',
            name='requirements',
            field=ckeditor.fields.RichTextField(),
        ),
    ]