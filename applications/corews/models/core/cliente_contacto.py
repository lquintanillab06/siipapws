from django.db import models
import uuid

from .cliente import Cliente

# REVISADA, Para descontinuar y eliminar

class ClienteContacto(models.Model):
    id = models.UUIDField(primary_key=True,default= uuid.uuid4, editable= False)
    version = models.BigIntegerField()
    telefono = models.CharField(max_length=255, blank=True, null=True)
    puesto = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING)
    email = models.CharField(max_length=255, blank=True, null=True)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    contactos_idx = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    last_updated = models.DateTimeField(auto_now=True, null= True)

    class Meta:
        managed = False
        db_table = 'cliente_contacto'