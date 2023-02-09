from django.db import models
import uuid

from .venta import Venta

class CondicionDeEnvio(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    version = models.BigIntegerField()
    fecha_de_entrega = models.DateTimeField()
    asegurado = models.BooleanField(default=False)
    grupo = models.CharField(max_length=10, blank=True, null=True)
    zona = models.CharField(max_length=20, blank=True, null=True)
    longitud = models.DecimalField(max_digits=19, decimal_places=2)
    venta = models.ForeignKey(Venta, models.DO_NOTHING)
    recoleccion = models.BooleanField(default=False)
    latitud = models.DecimalField(max_digits=19, decimal_places=2)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    condiciones = models.CharField(max_length=255, blank=True, null=True)
    asignado = models.DateTimeField(blank=True, null=True)
    ocurre = models.BooleanField(default=False)
    parcial = models.BooleanField(default=False)
    municipio = models.CharField(max_length=100, blank=True, null=True)
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
    transporte = models.CharField(max_length=255, blank=True, null=True)
    cerrado = models.DateTimeField(blank=True, null=True)
    comentario_cierre = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'condicion_de_envio'

