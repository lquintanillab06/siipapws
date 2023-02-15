from django.db import models

# REVISADA, sin cambio

class PolizaFolio(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    folio = models.IntegerField()
    date_created = models.DateTimeField()
    tipo = models.CharField(max_length=50)
    mes = models.IntegerField()
    last_updated = models.DateTimeField()
    ejercicio = models.IntegerField()
    subtipo = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'poliza_folio'
        unique_together = (('ejercicio', 'mes', 'subtipo', 'tipo', 'folio'),)