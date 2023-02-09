from django.db  import models
import uuid

from .cobro import Cobro
from ..core.banco import Banco
from ..core.cuenta_de_banco import CuentaDeBanco
from ..tesoreria.movimiento_cuenta import MovimientoDeCuenta


class CobroTransferencia(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    cobro = models.ForeignKey(Cobro, models.DO_NOTHING)
    last_updated = models.DateTimeField()
    cuenta_destino = models.ForeignKey(CuentaDeBanco, models.DO_NOTHING)
    folio = models.BigIntegerField()
    banco_origen = models.ForeignKey(Banco, models.DO_NOTHING)
    ingreso = models.ForeignKey(MovimientoDeCuenta, models.DO_NOTHING, blank=True, null=True)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    fecha_deposito = models.DateField()
    conciliado = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'cobro_transferencia'
