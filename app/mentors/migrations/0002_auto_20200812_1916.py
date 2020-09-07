# Generated by Django 3.1 on 2020-08-12 17:16

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import optimized_image.fields
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mentors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
            ],
        ),
        migrations.AlterModelOptions(
            name='mentor',
            options={'ordering': ['-created_date']},
        ),
        migrations.RenameField(
            model_name='historicalmentor',
            old_name='video_preview',
            new_name='video_presentation',
        ),
        migrations.RemoveField(
            model_name='mentor',
            name='video_preview',
        ),
        migrations.AddField(
            model_name='historicalmentor',
            name='slug',
            field=models.SlugField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='historicalmentor',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0),
        ),
        migrations.AddField(
            model_name='mentor',
            name='slug',
            field=models.SlugField(default='', max_length=150, unique=True),
        ),
        migrations.AddField(
            model_name='mentor',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0),
        ),
        migrations.AddField(
            model_name='mentor',
            name='video_presentation',
            field=models.FileField(blank=True, null=True, upload_to='mentors/video_presentation/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='historicalmentor',
            name='created_date',
            field=models.DateTimeField(blank=True, editable=False),
        ),
        migrations.AlterField(
            model_name='historicalmentor',
            name='published_date',
            field=models.DateTimeField(blank=True, editable=False),
        ),
        migrations.AlterField(
            model_name='historicalmentor',
            name='requirements',
            field=ckeditor.fields.RichTextField(verbose_name='Moje wymagania do ucznia'),
        ),
        migrations.AlterField(
            model_name='historicalmentor',
            name='what_can_i_teach_you',
            field=ckeditor.fields.RichTextField(verbose_name='Czego Cię nauczę?'),
        ),
        migrations.AlterField(
            model_name='historicalmentor',
            name='who_am_i',
            field=ckeditor.fields.RichTextField(verbose_name='Kim jestem?'),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='image_preview',
            field=optimized_image.fields.OptimizedImageField(upload_to='mentors/image_preview/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='published_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='requirements',
            field=ckeditor.fields.RichTextField(verbose_name='Moje wymagania do ucznia'),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='what_can_i_teach_you',
            field=ckeditor.fields.RichTextField(verbose_name='Czego Cię nauczę?'),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='who_am_i',
            field=ckeditor.fields.RichTextField(verbose_name='Kim jestem?'),
        ),
        migrations.CreateModel(
            name='HistoricalLanguage',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical language',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalCategory',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical category',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.AddField(
            model_name='historicalmentor',
            name='category',
            field=models.ForeignKey(blank=True, db_constraint=False, default='', help_text='Wybierz kategorię w której nauczasz', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='mentors.category', verbose_name='Kategoria'),
        ),
        migrations.AddField(
            model_name='historicalmentor',
            name='language',
            field=models.ForeignKey(blank=True, db_constraint=False, default='', help_text='Wybierz język w którym nauczasz', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='mentors.language', verbose_name='Język'),
        ),
        migrations.AddField(
            model_name='mentor',
            name='category',
            field=models.ForeignKey(default='', help_text='Wybierz kategorię w której nauczasz', on_delete=django.db.models.deletion.CASCADE, to='mentors.category', verbose_name='Kategoria'),
        ),
        migrations.AddField(
            model_name='mentor',
            name='language',
            field=models.ForeignKey(default='', help_text='Wybierz język w którym nauczasz', on_delete=django.db.models.deletion.CASCADE, to='mentors.language', verbose_name='Język'),
        ),
    ]