# Generated by Django 3.0.6 on 2020-05-22 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MantenedorSalas', '0004_auto_20200521_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horario',
            name='hora_inicio',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='horario',
            name='hora_termino',
            field=models.TimeField(),
        ),
    ]
