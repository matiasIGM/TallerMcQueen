# Generated by Django 3.2.4 on 2021-07-14 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210713_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrusel',
            name='clase',
            field=models.CharField(default=2, max_length=30, verbose_name='clase del slide'),
            preserve_default=False,
        ),
    ]
