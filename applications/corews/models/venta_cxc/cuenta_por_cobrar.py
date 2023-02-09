from django.db import models
import uuid

from ..core.sucursal import Sucursal
from ..core.cliente import Cliente
from .cfdi import Cfdi
from .venta_credito import VentaCredito


class CuentaPorCobrar(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    version = models.BigIntegerField()
    total = models.DecimalField(max_digits=19, decimal_places=2)
    tipo_documento = models.CharField(max_length=18)
    forma_de_pago = models.CharField(max_length=255)
    uuid = models.CharField(unique=True, max_length=255, blank=True, null=True)
    sucursal = models.ForeignKey(Sucursal, models.DO_NOTHING)
    moneda = models.CharField(max_length=255)
    tipo_de_cambio = models.DecimalField(max_digits=19, decimal_places=6)
    cargo = models.DecimalField(max_digits=19, decimal_places=2)
    update_user = models.CharField(max_length=255)
    tipo = models.CharField(max_length=3, blank=True, null=True)
    fecha = models.DateField()
    comentario = models.CharField(max_length=255, blank=True, null=True)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    impuesto = models.DecimalField(max_digits=19, decimal_places=2)
    documento = models.BigIntegerField()
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING)
    importe = models.DecimalField(max_digits=19, decimal_places=2)
    create_user = models.CharField(max_length=255)
    cfdi = models.ForeignKey(Cfdi, models.DO_NOTHING, blank=True, null=True)
    cancelacion_motivo = models.CharField(max_length=255, blank=True, null=True)
    descuento_importe = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    cheque_post_fechado = models.BooleanField(default=False)  
    cancelada = models.DateField(blank=True, null=True)
    subtotal = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    cancelacion_usuario = models.CharField(max_length=255, blank=True, null=True)
    credito = models.ForeignKey(VentaCredito, models.DO_NOTHING, blank=True, null=True)
    vencimiento = models.DateField(blank=True, null=True)
    juridico = models.DateField(blank=True, null=True)
    saldo_actualizado = models.FloatField(blank=True, null=True)
    anticipo = models.CharField(max_length=50, blank=True, null=True)
    anticipo_tipo = models.CharField(max_length=7, blank=True, null=True)
    relacionados = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    last_updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuenta_por_cobrar'
