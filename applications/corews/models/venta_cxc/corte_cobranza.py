from django.db import models
import uuid


from ..core.sucursal import Sucursal



class CorteCobranza(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    version = models.BigIntegerField()
    deposito = models.DecimalField(max_digits=19, decimal_places=2)
    forma_de_pago = models.CharField(max_length=255)
    cierre = models.BooleanField(default= False)
    cortes_acumulado = models.DecimalField(max_digits=19, decimal_places=2)
    sucursal = models.ForeignKey(Sucursal, models.DO_NOTHING)
    pagos_registrados = models.DecimalField(max_digits=19, decimal_places=2)
    tipo_de_venta = models.CharField(max_length=3)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    corte = models.DateTimeField()
    fecha = models.DateField()
    comentario = models.CharField(max_length=255, blank=True, null=True)
    fecha_deposito = models.DateField(blank=True, null=True)
    anticipo_corte = models.BooleanField(default=False)
    cambio_cheque = models.BooleanField(default=False)
    cambios_de_cheques = models.DecimalField(max_digits=19, decimal_places=2)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    last_updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'corte_cobranza'