# Generated by Django 3.2 on 2022-12-01 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('version', models.BigIntegerField(blank=True, default=1, null=True)),
                ('account_expired', models.BooleanField(default=False)),
                ('account_locked', models.BooleanField(default=False)),
                ('nombre', models.CharField(max_length=255)),
                ('nombres', models.CharField(max_length=255)),
                ('puesto', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('numero_de_empleado', models.IntegerField(blank=True, null=True)),
                ('enabled', models.BooleanField(default=False)),
                ('password', models.CharField(max_length=255)),
                ('password_expired', models.BooleanField(default=False)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('nip', models.CharField(blank=True, max_length=12, null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('sucursal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.sucursal')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'user',
                'managed': True,
            },
        ),
    ]
