# Generated by Django 3.1 on 2020-08-05 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_courselessons'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CourseLessons',
            new_name='CourseLesson',
        ),
    ]
