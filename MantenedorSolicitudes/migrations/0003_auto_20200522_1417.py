# Generated by Django 3.0.6 on 2020-05-22 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MantenedorSolicitudes', '0002_auto_20200521_1831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitud',
            name='horario_final',
        ),
        migrations.RemoveField(
            model_name='solicitud',
            name='horario_inicio',
        ),
        migrations.AddField(
            model_name='solicitud',
            name='fecha',
            field=models.DateField(default='2020-05-12'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solicitud',
            name='hora_final',
            field=models.TimeField(default='08:30'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solicitud',
            name='hora_inicio',
            field=models.TimeField(default='07:30'),
            preserve_default=False,
        ),
    ]
