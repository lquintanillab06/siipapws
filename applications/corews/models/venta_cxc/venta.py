from django.db import models
import uuid

from ..core.sucursal import Sucursal
from ..core.cliente import Cliente
from ..core.vendedor import Vendedor
from ..core.socio import Socio
from .cuenta_por_cobrar import CuentaPorCobrar



class Venta(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False )
    version = models.BigIntegerField()
    comision_tarjeta_importe = models.DecimalField(max_digits=19, decimal_places=2)
    vale = models.BooleanField(default=False)
    facturar = models.DateTimeField(blank=True, null=True)
    cfdi_mail = models.CharField(max_length=255, blank=True, null=True)
    total = models.DecimalField(max_digits=19, decimal_places=2)
    forma_de_pago = models.CharField(max_length=255)
    uso_de_cfdi = models.CharField(max_length=3, blank=True, null=True)
    kilos = models.DecimalField(max_digits=19, decimal_places=2)
    sucursal = models.ForeignKey(Sucursal, models.DO_NOTHING)
    descuento_original = models.DecimalField(max_digits=19, decimal_places=2)
    moneda = models.CharField(max_length=255)
    vendedor = models.ForeignKey(Vendedor, models.DO_NOTHING)
    atencion = models.CharField(max_length=10)
    corte_importe = models.DecimalField(max_digits=19, decimal_places=2)
    puesto = models.DateTimeField(blank=True, null=True)
    clasificacion_vale = models.CharField(max_length=30, blank=True, null=True)
    impreso = models.DateTimeField(blank=True, null=True)
    tipo_de_cambio = models.DecimalField(max_digits=19, decimal_places=6)
    descuento_importe = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    update_user = models.CharField(max_length=100, blank=True, null=True)
    cod = models.BooleanField(default=False)
    descuento = models.DecimalField(max_digits=19, decimal_places=2)
    tipo = models.CharField(max_length=3)
    sucursal_vale = models.ForeignKey(Sucursal, models.DO_NOTHING, blank=True, null=True)
    fecha = models.DateField()
    comision_tarjeta = models.DecimalField(max_digits=19, decimal_places=2)
    cuenta_por_cobrar = models.ForeignKey(CuentaPorCobrar, models.DO_NOTHING, blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    sucursal_venta = models.ForeignKey(Sucursal, models.DO_NOTHING, blank=True, null=True)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    impuesto = models.DecimalField(max_digits=19, decimal_places=2)
    subtotal = models.DecimalField(max_digits=19, decimal_places=2)
    documento = models.BigIntegerField()
    cargos_por_maniobra = models.DecimalField(max_digits=19, decimal_places=2)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING)
    comprador = models.CharField(max_length=255, blank=True, null=True)
    parcial = models.BooleanField(default=False)
    importe = models.DecimalField(max_digits=19, decimal_places=2)
    create_user = models.CharField(max_length=100, blank=True, null=True)
    sin_existencia = models.BooleanField(default=False)
    socio = models.ForeignKey(Socio, models.DO_NOTHING, blank=True, null=True)
    cheque_post_fechado = models.BooleanField(default=False)
    facturar_usuario = models.CharField(max_length=255, blank=True, null=True)
    venta_ine = models.BooleanField(default=False)
    no_facturable = models.IntegerField(blank=True, null=True)
    surtido = models.IntegerField(blank=True, null=True)
    callcenter = models.BooleanField(default=False)
    callcenter_version = models.IntegerField(blank=True, null=True)
    last_updated = models.DateTimeField(auto_now_add=True)
    date_created = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'venta'