from django.db import models
import uuid

from .venta_det import VentaDet

class InstruccionCorte(models.Model):
    id = models.UUIDField(primary_key=True,default= uuid.uuid4, editable=False)
    version = models.BigIntegerField()
    ancho = models.DecimalField(max_digits=19, decimal_places=2)
    tipo = models.CharField(max_length=50, blank=True, null=True)
    cantidad = models.BigIntegerField()
    seleccion_calculo = models.CharField(max_length=255, blank=True, null=True)
    precio = models.DecimalField(max_digits=19, decimal_places=2)
    instruccion = models.CharField(max_length=255, blank=True, null=True)
    venta_det = models.ForeignKey(VentaDet, models.DO_NOTHING)
    largo = models.DecimalField(max_digits=19, decimal_places=2)
    instruccion_empacado = models.CharField(max_length=255, blank=True, null=True)
    refinado = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'instruccion_corte'




