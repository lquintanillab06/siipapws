from django.db import models

class UnidadSat(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    clave_unidad_sat = models.CharField(max_length=255, blank=True, null=True)
    unidad_sat = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null= True)
    last_updated = models.DateTimeField(auto_now=True, null= True)

    class Meta:
        managed = True
        db_table = 'unidad_sat'