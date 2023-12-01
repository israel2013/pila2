# Generated by Django 4.2 on 2023-11-30 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0007_articulo_fecha_creacion_articulo_tracklist_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articulo',
            name='fecha_creacion',
        ),
        migrations.AddField(
            model_name='articulo',
            name='artista',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
