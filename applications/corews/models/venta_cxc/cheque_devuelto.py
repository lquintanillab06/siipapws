from django.db import models
import uuid

from .cobro_cheque import CobroCheque
from .cuenta_por_cobrar import CuentaPorCobrar
from ..tesoreria.movimiento_cuenta import MovimientoDeCuenta
from nota_cargo import NotaDeCargo

class ChequeDevuelto(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    version = models.BigIntegerField()
    folio = models.BigIntegerField()
    cheque = models.OneToOneField(CobroCheque, models.DO_NOTHING)
    
    comentario = models.CharField(max_length=255, blank=True, null=True)
   
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    nombre = models.CharField(max_length=255)
    cxc = models.ForeignKey(CuentaPorCobrar, models.DO_NOTHING)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    recepcion = models.DateField(blank=True, null=True)
    egreso = models.OneToOneField(MovimientoDeCuenta, models.DO_NOTHING, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    numero = models.CharField(max_length=255, blank=True, null=True)
    importe = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    nota_de_cargo = models.ForeignKey(NotaDeCargo, models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    last_updated = models.DateTimeField(auto_now=True, null=True)


    class Meta:
        managed = False
        db_table = 'cheque_devuelto'