from django.db import models
import uuid

from .venta_det import VentaDet
from ..core.producto import Producto

class VentaParcialDet(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    version = models.BigIntegerField()
    valor = models.DecimalField(max_digits=19, decimal_places=2)
    instruccion_de_entrega_parcial = models.CharField(max_length=255, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=19, decimal_places=2)
    venta_det = models.ForeignKey(VentaDet, models.DO_NOTHING, blank=True, null=True)
    producto = models.ForeignKey(Producto, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'venta_parcial_det'