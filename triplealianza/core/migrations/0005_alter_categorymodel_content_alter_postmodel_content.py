# Generated by Django 4.2 on 2023-04-19 22:36

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_categorymodel_featured_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorymodel',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Contenido'),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Contenido'),
        ),
    ]