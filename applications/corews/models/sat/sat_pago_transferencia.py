from django.db import models


class SatPagoTransferencia(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    monto = models.DecimalField(max_digits=19, decimal_places=2)
    fecha = models.DateTimeField()
    banco_ori_ext = models.CharField(max_length=255, blank=True, null=True)
    cta_dest = models.CharField(max_length=255)
    moneda = models.CharField(max_length=255, blank=True, null=True)
    banco_dest_nal = models.CharField(max_length=255)
    rfc = models.CharField(max_length=255)
    banco_dest_ext = models.CharField(max_length=255)
    tip_camb = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    banco_ori_nal = models.CharField(max_length=255)
    benef = models.CharField(max_length=255)
    cta_ori = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sat_pago_transferencia'