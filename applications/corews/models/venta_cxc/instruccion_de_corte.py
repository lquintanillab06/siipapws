from django.db import models
import uuid

from .venta_parcial_det import VentaParcialDet
from .surtido import Surtido

class InstruccionDeCorte(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    version = models.BigIntegerField()
    cantidad = models.DecimalField(max_digits=19, decimal_places=2)
    cortes = models.BigIntegerField()
    cortes_ancho = models.DecimalField(max_digits=19, decimal_places=2)
    cortes_instruccion = models.CharField(max_length=255)
    cortes_largo = models.DecimalField(max_digits=19, decimal_places=2)
    cortes_tipo = models.CharField(max_length=11)
    entidad = models.CharField(max_length=3)
    importe_empacado = models.DecimalField(max_digits=19, decimal_places=2)
    instruccion_empacado = models.CharField(max_length=255)
    origen_det = models.CharField(max_length=255)
    parcial_det = models.ForeignKey(VentaParcialDet, models.DO_NOTHING, blank=True, null=True)
    precio_cortes = models.DecimalField(max_digits=19, decimal_places=2)
    refinado = models.BooleanField(default=False)
    seleccion_calculo = models.CharField(max_length=10)
    surtido = models.ForeignKey(Surtido, models.DO_NOTHING)
    tamaños = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'instruccion_de_corte'