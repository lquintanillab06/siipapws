from django.db import models
import uuid

from ..core.socio import Socio
from ..core.cobrador import Cobrador

class VentaCredito(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    version = models.BigIntegerField()
    operador = models.IntegerField()
    fecha_pago = models.DateField()
    reprogramar_pago = models.DateField(blank=True, null=True)
    plazo = models.IntegerField()
    revisada = models.BooleanField(default=False)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    fecha_revision = models.DateField()
    fecha_revision_cxc = models.DateField()
    descuento = models.DecimalField(max_digits=19, decimal_places=2)
    socio = models.ForeignKey(Socio, models.DO_NOTHING, blank=True, null=True)
    cobrador = models.ForeignKey(Cobrador, models.DO_NOTHING)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    vencimiento = models.DateField()
    comentario_reprogramar_pago = models.CharField(max_length=255, blank=True, null=True)
    dia_revision = models.IntegerField()
    dia_pago = models.IntegerField()
    vencimiento_factura = models.BooleanField(default=False)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    fecha_recepcion_cxc = models.DateField(blank=True, null=True)
    revision = models.BooleanField(default= False)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    saldo = models.FloatField(blank=True, null=True)
    actualizacion = models.DateTimeField(blank=True, null=True)
    atraso = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'venta_credito'
