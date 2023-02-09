from django.db import models
import uuid

from ..tesoreria.corte_tarjeta import CorteDeTarjeta
from .cobro import Cobro


class CobroTarjeta(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    corte_de_tarjeta = models.ForeignKey(CorteDeTarjeta, models.DO_NOTHING, blank=True, null=True)
    comision = models.DecimalField(max_digits=19, decimal_places=2)
    debito_credito = models.BooleanField(default=True)
    
    cobro = models.ForeignKey(Cobro, models.DO_NOTHING)
    visa_master = models.BooleanField(default=True)
    
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    validacion = models.IntegerField()
    partidas_idx = models.IntegerField(blank=True, null=True)
    corte = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    last_updated = models.DateTimeField(auto_now=True,null=True)

    class Meta:
        managed = False
        db_table = 'cobro_tarjeta'