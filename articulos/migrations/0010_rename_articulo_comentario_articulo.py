# Generated by Django 4.2 on 2023-12-06 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0009_articulo_fecha_creacion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='articulo',
            new_name='Articulo',
        ),
    ]