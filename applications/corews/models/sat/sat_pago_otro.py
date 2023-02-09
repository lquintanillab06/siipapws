from django.db import models

class SatPagoOtro(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    monto = models.DecimalField(max_digits=19, decimal_places=2)
    fecha = models.DateTimeField()
    met_pago_pol = models.CharField(max_length=255)
    moneda = models.CharField(max_length=255, blank=True, null=True)
    rfc = models.CharField(max_length=255)
    tip_camb = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    benef = models.CharField(max_length=255)
    asiento = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sat_pago_otro'
