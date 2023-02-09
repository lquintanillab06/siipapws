from django.db import models
import uuid

from .ficha import Ficha
from .cobro import Cobro


class FichaDet(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    version = models.BigIntegerField()
    ficha = models.ForeignKey(Ficha, models.DO_NOTHING)
    cheque = models.DecimalField(max_digits=19, decimal_places=2)
    banco = models.CharField(max_length=50)
    cobro = models.ForeignKey(Cobro, models.DO_NOTHING)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    efectivo = models.DecimalField(max_digits=19, decimal_places=2)
    partidas_idx = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    last_updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'ficha_det'