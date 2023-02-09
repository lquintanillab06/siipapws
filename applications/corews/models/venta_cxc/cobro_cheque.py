from django.db import models
import uuid

from .cobro import Cobro
from .ficha import Ficha
from ..core.banco import Banco

class CobroCheque(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    version = models.BigIntegerField()
    ficha = models.ForeignKey(Ficha, models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField()
    cobro = models.ForeignKey(Cobro, models.DO_NOTHING)
    cambio_por_efectivo = models.BooleanField(default=False)
    emisor = models.CharField(max_length=255, blank=True, null=True)
    numero_de_cuenta = models.CharField(max_length=255)
    numero = models.BigIntegerField(blank=True, null=True)
    banco_origen = models.ForeignKey(Banco, models.DO_NOTHING)
    vencimiento = models.DateField(blank=True, null=True)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    post_fechado = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    last_updated = models.DateTimeField(auto_now=True,null=True)

    class Meta:
        managed = False
        db_table = 'cobro_cheque'