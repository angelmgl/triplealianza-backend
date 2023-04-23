# Generated by Django 4.2 on 2023-04-22 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_rename_image_imagemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='SliderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Título')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('button_url', models.CharField(max_length=50, verbose_name='Enlace del botón')),
                ('button_label', models.CharField(max_length=50, verbose_name='Texto del botón')),
                ('featured_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.imagemodel')),
            ],
        ),
    ]