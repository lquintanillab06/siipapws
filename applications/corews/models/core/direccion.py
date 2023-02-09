from django.db import models


class Direccion(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    numero_exterior = models.CharField(max_length=50, blank=True, null=True)
    numero_interior = models.CharField(max_length=50, blank=True, null=True)
    latitud = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    longitud = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    estado = models.CharField(max_length=255, blank=True, null=True)
    pais = models.CharField(max_length=100, blank=True, null=True)
    calle = models.CharField(max_length=200, blank=True, null=True)
    colonia = models.CharField(max_length=255, blank=True, null=True)
    codigo_postal = models.CharField(max_length=255, blank=True, null=True)
    municipio = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'direccion'