from django.db import models
import uuid

from .venta import Venta

class VentaAnticipo(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    version = models.BigIntegerField()
    venta = models.ForeignKey(Venta, models.DO_NOTHING)
    importe = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'venta_anticipo'
