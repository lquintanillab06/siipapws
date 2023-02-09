from django.db import models


class UnidadSat(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    clave_unidad_sat = models.CharField(max_length=255, blank=True, null=True)
    unidad_sat = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unidad_sat'
