# Generated by Django 4.2 on 2023-04-22 03:06

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_menumodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Título')),
                ('seo_title', models.CharField(default='', max_length=150, verbose_name='Título SEO')),
                ('slug', models.CharField(max_length=150, unique=True, verbose_name='Slug URL')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('featured_image', models.ImageField(upload_to='files', verbose_name='Imagen destacada')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Contenido')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Última edición')),
            ],
            options={
                'verbose_name': 'Página',
                'verbose_name_plural': 'Páginas',
            },
        ),
        migrations.AlterModelOptions(
            name='menumodel',
            options={'ordering': ['order'], 'verbose_name': 'Enlace del menú', 'verbose_name_plural': 'Enlaces del menú'},
        ),
    ]
