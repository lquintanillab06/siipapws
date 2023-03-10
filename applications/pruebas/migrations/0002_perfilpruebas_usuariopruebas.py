# Generated by Django 3.2 on 2023-01-06 12:33

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('pruebas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsuarioPruebas',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'usuario_pruebas',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PerfilPruebas',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('nip', models.CharField(max_length=100)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pruebas.usuariopruebas')),
            ],
            options={
                'db_table': 'perfil_pruebas',
                'managed': True,
            },
        ),
    ]
