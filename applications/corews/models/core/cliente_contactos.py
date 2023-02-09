from django.db import models
import uuid

from .cliente import Cliente


class ClienteContactos(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    version = models.BigIntegerField()
    activo = models.BooleanField(default=True) 
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING)
    email = models.CharField(max_length=255, blank=True, null=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    puesto = models.CharField(max_length=255, blank=True, null=True)
    sw2 = models.BigIntegerField(blank=True, null=True)
    telefono = models.CharField(max_length=255, blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'cliente_contactos'