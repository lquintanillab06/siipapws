from django.db import models
import uuid

from .chofer import Chofer
from .sucursal import Sucursal
from .embarque import Embarque

# REVISADA, Logistaca PapelSA - Se reactivo embarque_id para uso 

class ChoferUbicacion(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable= False)
    version = models.BigIntegerField()
    chofer = models.ForeignKey(Chofer, models.DO_NOTHING)
    embarque = models.ForeignKey(Embarque, models.DO_NOTHING, blank=True, null=True)
    fecha = models.DateTimeField()
    incidencia = models.CharField(max_length=255, blank=True, null=True)
    latitud = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    longitud = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    sucursal = models.ForeignKey(Sucursal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'chofer_ubicacion'
