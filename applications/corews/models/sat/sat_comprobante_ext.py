from django.db import models
import uuid

class SatComprobanteExt(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    num_fact_ext = models.CharField(max_length=255)
    monto_total = models.DecimalField(max_digits=19, decimal_places=2)
    taxid = models.CharField(max_length=255, blank=True, null=True)
    moneda = models.CharField(max_length=255, blank=True, null=True)
    tip_camb = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sat_comprobante_ext'