# Generated by Django 4.0.5 on 2022-06-22 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='telefono',
            field=models.IntegerField(verbose_name='Telefono'),
        ),
    ]
