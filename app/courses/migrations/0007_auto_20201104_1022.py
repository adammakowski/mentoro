# Generated by Django 3.1.2 on 2020-11-04 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_lesson_free_lesson'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'get_latest_by': ['-position'], 'verbose_name': 'Lesson', 'verbose_name_plural': 'Lessons'},
        ),
    ]
