from django.db import models
import uuid


class TransporteEmpresa(models.Model):
    id = models.UUIDField(primary_key=True,default= uuid.uuid4,editable= False)
    version = models.BigIntegerField()
    telefono3 = models.CharField(max_length=255, blank=True, null=True)
    telefono2 = models.CharField(max_length=255, blank=True, null=True)
    nombre = models.CharField(max_length=255)
    telefono1 = models.CharField(max_length=255, blank=True, null=True)
    direccion_numero_exterior = models.CharField(max_length=50, blank=True, null=True)
    direccion_numero_interior = models.CharField(max_length=50, blank=True, null=True)
    direccion_latitud = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    direccion_longitud = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    direccion_estado = models.CharField(max_length=255, blank=True, null=True)
    direccion_pais = models.CharField(max_length=100, blank=True, null=True)
    direccion_calle = models.CharField(max_length=200, blank=True, null=True)
    direccion_colonia = models.CharField(max_length=255, blank=True, null=True)
    direccion_codigo_postal = models.CharField(max_length=255, blank=True, null=True)
    direccion_municipio = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'transporte_empresa'