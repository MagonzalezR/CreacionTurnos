# Generated by Django 4.1.3 on 2022-11-19 04:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionTurnos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='user',
            name='nombre',
        ),
    ]
