from django.db import models
import uuid

from .venta import Venta
class ComplementoIne(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    version = models.BigIntegerField()
    contabilidad = models.BigIntegerField(blank=True, null=True)
    venta = models.ForeignKey(Venta, models.DO_NOTHING)
    tipo_de_comite = models.CharField(max_length=18, blank=True, null=True)
    tipo_de_proceso = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'complemento_ine'