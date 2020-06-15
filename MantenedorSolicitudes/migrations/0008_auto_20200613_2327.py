# Generated by Django 3.0.6 on 2020-06-14 03:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('MantenedorSolicitudes', '0007_auto_20200612_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud',
            name='fecha_creacion',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solicitud',
            name='fecha_eliminacion',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='fecha_modificacion',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='descripcion',
            field=models.TextField(max_length=150),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='respuesta',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
    ]
