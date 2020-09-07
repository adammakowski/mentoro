# Generated by Django 3.1 on 2020-08-17 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentors', '0008_auto_20200817_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalmentor',
            name='price',
            field=models.DecimalField(decimal_places=2, default='50', max_digits=7),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='price',
            field=models.DecimalField(decimal_places=2, default='50', max_digits=7),
        ),
    ]
