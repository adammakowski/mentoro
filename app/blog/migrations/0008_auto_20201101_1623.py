# Generated by Django 3.1.2 on 2020-11-01 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20201101_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.CharField(choices=[('Negatywna ocena', 'Negatywna ocena'), ('Pozytywna ocena', 'Pozytywna ocena')], help_text='Twoja ocena postu', max_length=100, verbose_name='Ocena'),
        ),
    ]
