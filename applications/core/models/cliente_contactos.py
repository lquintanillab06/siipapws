from django.db import models
import uuid

from . import Cliente

class ClienteContactos(models.Model):
    id = models.UUIDField(primary_key= True, default= uuid.uuid4, editable= False)
    version = models.BigIntegerField()
    activo = models.BooleanField(default= False)
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING, null= True)
    email = models.CharField(max_length=255, blank=True, null=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    puesto = models.CharField(max_length=255, blank=True, null=True)
    sw2 = models.BigIntegerField(blank=True, null=True)
    telefono = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null= True)
    last_updated = models.DateTimeField(auto_now=True, null= True)
    

    class Meta:
        managed = True
        db_table = 'cliente_contactos'