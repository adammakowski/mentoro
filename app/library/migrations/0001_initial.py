# Generated by Django 3.0.6 on 2020-05-23 15:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import optimized_image.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LibraryCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='LibraryLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='LibraryFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=150)),
                ('price', models.DecimalField(decimal_places=2, default='9.99', max_digits=7)),
                ('short_description', models.TextField(default='', max_length=500)),
                ('description', models.TextField(default='')),
                ('image_preview', optimized_image.fields.OptimizedImageField(default='', upload_to='image_library_preview/%Y/%m/%d/')),
                ('video_preview', models.FileField(default='', upload_to='video_library_preview/%Y/%m/%d/')),
                ('file_download', models.FileField(default='', upload_to='files_library/%Y/%m/%d/')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='library.LibraryCategory')),
                ('language', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='library.LibraryLanguage')),
            ],
        ),
    ]
