from django.db import models

from ..core.cuenta_de_banco import CuentaDeBanco
from ..core.sucursal import Sucursal
from ..tesoreria.movimiento_cuenta import MovimientoDeCuenta

class Ficha(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    total = models.DecimalField(max_digits=19, decimal_places=2)
    cuenta_de_banco = models.ForeignKey(CuentaDeBanco, models.DO_NOTHING)  
    tipo_de_ficha = models.CharField(max_length=12)
    sucursal = models.ForeignKey(Sucursal, models.DO_NOTHING)
    fecha_corte = models.DateTimeField(blank=True, null=True)
    origen = models.CharField(max_length=3)
    folio = models.BigIntegerField()
    fecha = models.DateField()
    cancelada = models.DateTimeField(blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    ingreso = models.ForeignKey(MovimientoDeCuenta, models.DO_NOTHING, blank=True, null=True)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    envio_valores = models.BooleanField(default=False)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    diferencia_tipo = models.CharField(max_length=12, blank=True, null=True)
    diferencia_usuario = models.CharField(max_length=255, blank=True, null=True)
    diferencia = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    last_updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'ficha'