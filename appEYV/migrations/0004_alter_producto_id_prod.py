# Generated by Django 4.2.2 on 2024-11-06 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appEYV', '0003_alter_producto_id_prod_alter_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='ID_prod',
            field=models.IntegerField(max_length=3, unique=True),
        ),
    ]
