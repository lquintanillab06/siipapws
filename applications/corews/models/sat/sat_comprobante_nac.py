from django.db import models


class SatComprobanteNac(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    uuidcfdi = models.CharField(max_length=255)
    monto_total = models.DecimalField(max_digits=19, decimal_places=2)
    moneda = models.CharField(max_length=255, blank=True, null=True)
    rfc = models.CharField(max_length=255)
    tip_camb = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sat_comprobante_nac'