# Generated by Django 3.2 on 2023-01-09 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pruebas', '0003_alter_perfilpruebas_usuario'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuariopruebas',
            options={'managed': True, 'permissions': [('set_password', 'Can set the password')]},
        ),
    ]
