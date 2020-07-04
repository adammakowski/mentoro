# Generated by Django 3.0.7 on 2020-06-26 15:17

from django.db import migrations, models
import optimized_image.fields


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_auto_20200626_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicallibraryfile',
            name='file_download',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='historicallibraryfile',
            name='image_preview',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='libraryfile',
            name='file_download',
            field=models.FileField(upload_to='library/files_library/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='libraryfile',
            name='image_preview',
            field=optimized_image.fields.OptimizedImageField(upload_to='library/image_library_preview/%Y/%m/%d/'),
        ),
    ]
