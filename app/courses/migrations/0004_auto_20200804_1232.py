# Generated by Django 3.1 on 2020-08-04 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20200804_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='video_preview',
            field=models.FileField(help_text='Dodaj film wideo reklamujący i prezentująćy Twoj wideo kurs', upload_to='courses/video_course_preview/%Y/%m/%d/', verbose_name='Wideo prezentacja'),
        ),
    ]