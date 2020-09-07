# Generated by Django 3.1 on 2020-08-17 21:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mentors', '0005_auto_20200817_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentor',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mentors', to=settings.AUTH_USER_MODEL),
        ),
    ]
