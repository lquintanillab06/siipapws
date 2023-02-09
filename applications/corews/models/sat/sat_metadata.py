from django.db import models

class SatMetadata(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    pac_rfc = models.CharField(max_length=15)
    emisor_nombre = models.CharField(max_length=255)
    recepctor_nombre = models.CharField(max_length=255)
    uuid = models.CharField(max_length=70)
    estatus = models.CharField(max_length=5)
    ejercicio = models.IntegerField()
    fecha_emision = models.DateTimeField()
    monto = models.DecimalField(max_digits=19, decimal_places=2)
    mes = models.IntegerField()
    receptor_rfc = models.CharField(max_length=15)
    fecha_cancelacion = models.DateTimeField(blank=True, null=True)
    fecha_certificacion_sat = models.DateTimeField()
    efecto_comprobante = models.CharField(max_length=255)
    emisor_rfc = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'sat_metadata'