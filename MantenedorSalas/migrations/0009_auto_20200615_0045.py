# Generated by Django 3.0.6 on 2020-06-15 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MantenedorSalas', '0008_auto_20200523_2118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='horario',
            name='sala',
        ),
        migrations.AddField(
            model_name='horario',
            name='sala',
            field=models.ManyToManyField(related_name='horarios', to='MantenedorSalas.Sala'),
        ),
    ]
