# Generated by Django 4.2.2 on 2024-11-28 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appEYV', '0006_alter_producto_tipo_prod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='Tipo_prod',
            field=models.IntegerField(choices=[(0, 'Linterna'), (1, 'Herramienta')], max_length=30),
        ),
    ]