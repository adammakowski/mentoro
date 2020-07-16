# Generated by Django 3.0.8 on 2020-07-13 17:07

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import optimized_image.fields


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0019_auto_20200710_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicallibraryfile',
            name='category',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='Wybierz kategorię w której chcesz dodać wpis', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='library.LibraryCategory', verbose_name='Kategoria'),
        ),
        migrations.AlterField(
            model_name='historicallibraryfile',
            name='contests',
            field=ckeditor.fields.RichTextField(help_text='Podaj zawartość i spis treści Twojego materiału', verbose_name='Zawartość i spis treści'),
        ),
        migrations.AlterField(
            model_name='historicallibraryfile',
            name='description',
            field=ckeditor.fields.RichTextField(help_text='Podaj szczegółowy opis Twojego materiału.', verbose_name='Szczegółowy opis'),
        ),
        migrations.AlterField(
            model_name='historicallibraryfile',
            name='file_download',
            field=models.TextField(help_text='Dodaj plik który kupujący będzie mógł pobrać. Dozwolone formaty to: zip, rar, pdf, txt, epub', max_length=100, verbose_name='Plik do pobrania'),
        ),
        migrations.AlterField(
            model_name='historicallibraryfile',
            name='image_preview',
            field=models.TextField(help_text='Dodaj zdjęcie podglądowe materiału', max_length=100, verbose_name='Zdjęcie podglądowe'),
        ),
        migrations.AlterField(
            model_name='historicallibraryfile',
            name='language',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='Wybierz język w którym są Twoje treści', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='library.LibraryLanguage', verbose_name='Język'),
        ),
        migrations.AlterField(
            model_name='historicallibraryfile',
            name='price',
            field=models.DecimalField(decimal_places=2, help_text='Podaj cenę w złotówkach za która chcesz sprzedawać materiał', max_digits=7, verbose_name='Cena'),
        ),
        migrations.AlterField(
            model_name='historicallibraryfile',
            name='requirements',
            field=ckeditor.fields.RichTextField(help_text='Wymagana wiedza do zrozumienia materiału', verbose_name='Wymagana wiedza'),
        ),
        migrations.AlterField(
            model_name='historicallibraryfile',
            name='short_description',
            field=ckeditor.fields.RichTextField(help_text='Dodaj krótki opis. Maksymalna ilość znaków to 500', max_length=500, verbose_name='Krótki opis'),
        ),
        migrations.AlterField(
            model_name='historicallibraryfile',
            name='title',
            field=models.CharField(help_text='Podaj tytuł wpisu który chcesz dodać', max_length=150, verbose_name='Tytuł'),
        ),
        migrations.AlterField(
            model_name='historicallibraryfile',
            name='video_preview',
            field=models.TextField(blank=True, help_text='Dodaj film wideo reklamujący i opisujący Twoj materiał', max_length=100, null=True, verbose_name='Wideo wprowadzające'),
        ),
        migrations.AlterField(
            model_name='libraryfile',
            name='category',
            field=models.ForeignKey(help_text='Wybierz kategorię w której chcesz dodać wpis', on_delete=django.db.models.deletion.CASCADE, to='library.LibraryCategory', verbose_name='Kategoria'),
        ),
        migrations.AlterField(
            model_name='libraryfile',
            name='contests',
            field=ckeditor.fields.RichTextField(help_text='Podaj zawartość i spis treści Twojego materiału', verbose_name='Zawartość i spis treści'),
        ),
        migrations.AlterField(
            model_name='libraryfile',
            name='description',
            field=ckeditor.fields.RichTextField(help_text='Podaj szczegółowy opis Twojego materiału.', verbose_name='Szczegółowy opis'),
        ),
        migrations.AlterField(
            model_name='libraryfile',
            name='file_download',
            field=models.FileField(help_text='Dodaj plik który kupujący będzie mógł pobrać. Dozwolone formaty to: zip, rar, pdf, txt, epub', upload_to='library/files_library/%Y/%m/%d/', verbose_name='Plik do pobrania'),
        ),
        migrations.AlterField(
            model_name='libraryfile',
            name='image_preview',
            field=optimized_image.fields.OptimizedImageField(help_text='Dodaj zdjęcie podglądowe materiału', upload_to='library/image_library_preview/%Y/%m/%d/', verbose_name='Zdjęcie podglądowe'),
        ),
        migrations.AlterField(
            model_name='libraryfile',
            name='language',
            field=models.ForeignKey(help_text='Wybierz język w którym są Twoje treści', on_delete=django.db.models.deletion.CASCADE, to='library.LibraryLanguage', verbose_name='Język'),
        ),
        migrations.AlterField(
            model_name='libraryfile',
            name='price',
            field=models.DecimalField(decimal_places=2, help_text='Podaj cenę w złotówkach za która chcesz sprzedawać materiał', max_digits=7, verbose_name='Cena'),
        ),
        migrations.AlterField(
            model_name='libraryfile',
            name='requirements',
            field=ckeditor.fields.RichTextField(help_text='Wymagana wiedza do zrozumienia materiału', verbose_name='Wymagana wiedza'),
        ),
        migrations.AlterField(
            model_name='libraryfile',
            name='short_description',
            field=ckeditor.fields.RichTextField(help_text='Dodaj krótki opis. Maksymalna ilość znaków to 500', max_length=500, verbose_name='Krótki opis'),
        ),
        migrations.AlterField(
            model_name='libraryfile',
            name='title',
            field=models.CharField(help_text='Podaj tytuł wpisu który chcesz dodać', max_length=150, verbose_name='Tytuł'),
        ),
        migrations.AlterField(
            model_name='libraryfile',
            name='video_preview',
            field=models.FileField(blank=True, help_text='Dodaj film wideo reklamujący i opisujący Twoj materiał', null=True, upload_to='library/video_library_preview/%Y/%m/%d/', verbose_name='Wideo wprowadzające'),
        ),
    ]
