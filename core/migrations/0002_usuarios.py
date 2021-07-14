# Generated by Django 3.2.4 on 2021-07-13 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('idUsuario', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Id de Usuario')),
                ('nombre', models.CharField(max_length=30, verbose_name='nombre del usuario')),
                ('apellido', models.CharField(max_length=30, verbose_name='apellido del usuario')),
                ('email', models.CharField(max_length=40, verbose_name='email del usuario')),
                ('contraseña', models.CharField(max_length=20, verbose_name='contraseña del usuario')),
            ],
        ),
    ]
