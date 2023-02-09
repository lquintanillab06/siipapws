from django.db import models
import uuid


from .cobro import Cobro
from ..core.cuenta_de_banco import CuentaDeBanco
from ..core.banco import Banco
from ..tesoreria.movimiento_cuenta import MovimientoDeCuenta

class CobroDeposito(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    version = models.BigIntegerField() 
    cobro = models.ForeignKey(Cobro, models.DO_NOTHING)
    total_efectivo = models.DecimalField(max_digits=19, decimal_places=2)
    cuenta_destino = models.ForeignKey(CuentaDeBanco, models.DO_NOTHING)
    folio = models.BigIntegerField()
    banco_origen = models.ForeignKey(Banco, models.DO_NOTHING)
    total_cheque = models.DecimalField(max_digits=19, decimal_places=2)
    ingreso = models.ForeignKey(MovimientoDeCuenta, models.DO_NOTHING, blank=True, null=True)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    fecha_deposito = models.DateField()
    total_tarjeta = models.DecimalField(max_digits=19, decimal_places=2)
    conciliado = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now_add=True)
    date_created = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cobro_deposito'