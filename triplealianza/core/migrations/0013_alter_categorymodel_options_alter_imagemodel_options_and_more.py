# Generated by Django 4.2 on 2023-04-22 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_slidemodel_delete_slidermodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorymodel',
            options={'verbose_name': 'categoría', 'verbose_name_plural': 'categorías'},
        ),
        migrations.AlterModelOptions(
            name='imagemodel',
            options={'verbose_name': 'imagen', 'verbose_name_plural': 'imágenes'},
        ),
        migrations.AlterModelOptions(
            name='menumodel',
            options={'ordering': ['order'], 'verbose_name': 'enlace del menú', 'verbose_name_plural': 'enlaces del menú'},
        ),
        migrations.AlterModelOptions(
            name='pagemodel',
            options={'verbose_name': 'página', 'verbose_name_plural': 'páginas'},
        ),
        migrations.AlterModelOptions(
            name='postmodel',
            options={'verbose_name': 'publicación', 'verbose_name_plural': 'publicaciones'},
        ),
        migrations.AlterModelOptions(
            name='slidemodel',
            options={'ordering': ['order'], 'verbose_name': 'slide', 'verbose_name_plural': 'slides'},
        ),
    ]
