from django.db import models
import uuid

from .cobro import Cobro
from .cuenta_por_cobrar import CuentaPorCobrar

class AplicacionDeCobro(models.Model):
    id = models.UUIDField(primary_key=True,)
    version = models.BigIntegerField()
    cobro = models.ForeignKey(Cobro, models.DO_NOTHING, blank=True, null=True)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    fecha = models.DateField()
    cuenta_por_cobrar = models.ForeignKey(CuentaPorCobrar, models.DO_NOTHING)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    importe = models.DecimalField(db_column='IMPORTE', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    create_user = models.CharField(max_length=255, blank=True, null=True)
    aplicaciones_idx = models.IntegerField(blank=True, null=True)
    forma_de_pago = models.CharField(max_length=255, blank=True, null=True)
    nota_de_credito_id = models.BigIntegerField(blank=True, null=True)
    recibo = models.CharField(max_length=255, blank=True, null=True)
    tipo_de_cambio = models.DecimalField(max_digits=19, decimal_places=8, blank=True, null=True)
    moneda = models.CharField(max_length=3, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    last_updated = models.DateTimeField(auto_now=True,null=True)

    class Meta:
        managed = False
        db_table = 'aplicacion_de_cobro'