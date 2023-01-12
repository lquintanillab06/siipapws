from django.db import models
import uuid

class MarcaPruebas(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    version = models.BigIntegerField()
    activa = models.BooleanField(default=True)
    marca = models.CharField(unique=True, max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'marca_pruebas'

class UsuarioPruebas(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    class Meta:
        managed = True
        db_table = 'usuario_pruebas'
        permissions =[ ('set_password','Can set the password')]


class PerfilPruebas(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=100)
    nip = models.CharField(max_length=100)
    usuario = models.ForeignKey(UsuarioPruebas,on_delete= models.CASCADE, related_name='perfil')
    class Meta:
        managed = True
        db_table = 'perfil_pruebas'



