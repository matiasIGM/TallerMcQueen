# Generated by Django 3.2.4 on 2021-07-13 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_usuarios'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrusel',
            fields=[
                ('idCarrusel', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Id Carrusel')),
                ('enlaceImagen', models.CharField(max_length=50, verbose_name='Enlace de imagen')),
            ],
        ),
        migrations.CreateModel(
            name='Mecanicos',
            fields=[
                ('idMecanico', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Id de Usuario')),
                ('nombreMecanico', models.CharField(max_length=20, verbose_name='Nombre del mecanico')),
                ('apellidoMecanico', models.CharField(max_length=20, verbose_name='Apellido del mecanico')),
                ('edad', models.IntegerField(max_length=2, verbose_name='Edad del mecanico')),
                ('especialidad', models.CharField(max_length=40, verbose_name='Especialidad del mecanico')),
                ('imagenMecanico', models.CharField(max_length=40, verbose_name='Imagen del mecanico')),
            ],
        ),
    ]
