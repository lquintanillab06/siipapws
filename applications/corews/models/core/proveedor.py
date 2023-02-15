from django.db import models
import uuid

# REVISADA, Se quito sw2 y "clave (para descontinuar la contabilidad no la sua y compras tiene buscador por nombre)"

class Proveedor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    version = models.BigIntegerField()
    activo =  models.BooleanField(default=True)    
    cuenta_bancaria = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    nacional = models.BooleanField(default=True)
    nombre = models.CharField(unique=True, max_length=255)
    rfc = models.CharField(max_length=13)    
    telefono1 = models.CharField(max_length=30, blank=True, null=True)
    telefono2 = models.CharField(max_length=30, blank=True, null=True)
    telefono3 = models.CharField(max_length=30, blank=True, null=True)
    tipo = models.CharField(max_length=26)
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
    plazo = models.IntegerField()
    fecha_revision = models.IntegerField(blank=True, null=True)
    imprimir_costo = models.IntegerField(blank=True, null=True)
    descuentof = models.BigIntegerField(blank=True, null=True)
    diasdf = models.BigIntegerField(blank=True, null=True)
    limite_de_credito = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'proveedor'