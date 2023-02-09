from django.db import models
import uuid

from ..core.sucursal import Sucursal
from ..core.cliente import Cliente
from .cfdi import Cfdi

class Cobro(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable=False)
    version = models.BigIntegerField()
    diferencia_fecha = models.DateField(blank=True, null=True)
    anticipo = models.BooleanField(default=False)
    forma_de_pago = models.CharField(max_length=255)
    sucursal = models.ForeignKey(Sucursal, models.DO_NOTHING)
    referencia = models.CharField(max_length=255, blank=True, null=True)
    moneda = models.CharField(max_length=255)
    tipo_de_cambio = models.DecimalField(db_column='TIPO_DE_CAMBIO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    primera_aplicacion = models.DateTimeField(blank=True, null=True)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    diferencia = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    tipo = models.CharField(max_length=3)
    fecha = models.DateField()
    enviado = models.BooleanField(default=False)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING)
    importe = models.DecimalField(max_digits=19, decimal_places=2)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    cfdi = models.ForeignKey(Cfdi, models.DO_NOTHING, blank=True, null=True)
    #cancelacion_de_cfdi = models.ForeignKey(CancelacionDeCfdi, models.DO_NOTHING, blank=True, null=True)
    cancelacion_motivo = models.CharField(max_length=255, blank=True, null=True)
    recibo_anterior = models.CharField(max_length=100, blank=True, null=True)
    anticipo_sat = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    last_updated = models.DateTimeField(auto_now=True,null=True)

    class Meta:
        managed = False
        db_table = 'cobro'