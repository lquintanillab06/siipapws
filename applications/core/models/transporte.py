from django.db import models
import uuid

from .chofer import Chofer
from facturista_de_embarque import FacturistaDeEmbarque

class Transporte(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable= False, max_length=255)
    version = models.BigIntegerField()
    chofer = models.ForeignKey(Chofer, models.DO_NOTHING, blank=True, null=True)
    capacidad = models.DecimalField(max_digits=19, decimal_places=2)
    modelo = models.CharField(max_length=255, blank=True, null=True)
    numero = models.CharField(max_length=30)
    facturista = models.ForeignKey(FacturistaDeEmbarque, models.DO_NOTHING, blank=True, null=True)
    placa = models.CharField(max_length=255, blank=True, null=True)
    marca = models.CharField(max_length=255, blank=True, null=True)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.CharField(max_length=255)
    anio = models.CharField(max_length=255, blank=True, null=True)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'transporte'