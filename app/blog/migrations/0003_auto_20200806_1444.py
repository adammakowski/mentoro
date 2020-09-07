# Generated by Django 3.1 on 2020-08-06 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200806_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(help_text='Podaj tytuł wpisu który chcesz dodać', max_length=150, verbose_name='Tytuł'),
        ),
        migrations.AlterField(
            model_name='historicalblogpost',
            name='title',
            field=models.CharField(help_text='Podaj tytuł wpisu który chcesz dodać', max_length=150, verbose_name='Tytuł'),
        ),
    ]