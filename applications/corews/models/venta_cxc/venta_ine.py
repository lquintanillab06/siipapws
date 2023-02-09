from django.db import models
import uuid

from .venta import Venta
from .cfdi import Cfdi

class VentaIne(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    version = models.BigIntegerField()
    contabilidad = models.BigIntegerField()
    venta = models.ForeignKey(Venta, models.DO_NOTHING)
    tipo_de_proceso = models.CharField(max_length=255, blank=True, null=True)
    tipo_de_comite = models.CharField(max_length=255, blank=True, null=True)
    cfdi = models.ForeignKey(Cfdi, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'venta_ine'
