
from django.db import models
import uuid

# REVISADA, sin cambio

class Empresa(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    version = models.BigIntegerField()
    certificado_digital = models.TextField(blank=True, null=True)
    certificado_digital_pfx = models.TextField(blank=True, null=True)
    clave = models.CharField(unique=True, max_length=15)
    llave_privada = models.TextField(blank=True, null=True)
    nombre = models.CharField(unique=True, max_length=255)
    numero_de_certificado = models.CharField(max_length=20, blank=True, null=True)
    password_pac = models.CharField(max_length=255, blank=True, null=True)
    password_pfx = models.CharField(max_length=255, blank=True, null=True)
    regimen = models.CharField(max_length=300)
    rfc = models.CharField(max_length=13)
    timbrado_de_prueba = models.BooleanField(default=True) 
    usuario_pac = models.CharField(max_length=255, blank=True, null=True)
    direccion_calle = models.CharField(max_length=200, blank=True, null=True)
    direccion_codigo_postal = models.CharField(max_length=255, blank=True, null=True)
    direccion_colonia = models.CharField(max_length=255, blank=True, null=True)
    direccion_estado = models.CharField(max_length=255, blank=True, null=True)
    direccion_latitud = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    direccion_longitud = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    direccion_municipio = models.CharField(max_length=255, blank=True, null=True)
    direccion_numero_exterior = models.CharField(max_length=50, blank=True, null=True)
    direccion_numero_interior = models.CharField(max_length=50, blank=True, null=True)
    direccion_pais = models.CharField(max_length=100, blank=True, null=True)
    regimen_clave_sat = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'empresa'