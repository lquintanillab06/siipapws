from django.db import models
import uuid
from .facturista_de_embarque import FacturistaDeEmbarque

# REVISADO Y MODIFICADO - se quito sw2

class Chofer(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable= False)
    version = models.BigIntegerField()
    celular = models.CharField(max_length=255, blank=True, null=True)
    mail = models.CharField(max_length=255, blank=True, null=True)
    nombre = models.CharField(max_length=255)
    rfc = models.CharField(max_length=255, blank=True, null=True)    
    activo = models.BooleanField(default=True)
    comision = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    precio_tonelada = models.DecimalField(max_digits=19, decimal_places=2)
    facturista = models.ForeignKey(FacturistaDeEmbarque, models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=255, blank=True, null=True)
    last_updated_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'chofer'