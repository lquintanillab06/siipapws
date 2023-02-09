from django.db import models


class SatTransaccionCheque(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    monto = models.DecimalField(max_digits=19, decimal_places=2)
    ban_emis_nal = models.CharField(max_length=255)
    fecha = models.DateTimeField()
    ban_emis_ext = models.CharField(max_length=255, blank=True, null=True)
    moneda = models.CharField(max_length=255, blank=True, null=True)
    rfc = models.CharField(max_length=255)
    num = models.CharField(max_length=255)
    tip_camb = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    benef = models.CharField(max_length=255)
    cta_ori = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'sat_transaccion_cheque'