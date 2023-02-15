from django.db import models

# REVISADA, sin cambio

class TipoDeCambio(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    fecha = models.DateField()
    fuente = models.CharField(max_length=200)
    last_updated = models.DateTimeField()
    moneda = models.CharField(max_length=255)
    tipo_de_cambio = models.DecimalField(max_digits=19, decimal_places=6)

    class Meta:
        managed = False
        db_table = 'tipo_de_cambio'