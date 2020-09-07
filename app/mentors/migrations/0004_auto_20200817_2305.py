# Generated by Django 3.1 on 2020-08-17 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentors', '0003_auto_20200812_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalmentor',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mentor',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='historicalmentor',
            name='status',
            field=models.IntegerField(choices=[(0, 'Szkic'), (1, 'Publikacja')], default=0, help_text='Status publikacji'),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='status',
            field=models.IntegerField(choices=[(0, 'Szkic'), (1, 'Publikacja')], default=0, help_text='Status publikacji'),
        ),
    ]