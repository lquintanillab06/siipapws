from django.db import models
import uuid


from .cliente import Cliente

# *** Para proceso de Logistica PapelSA ***

class DireccionEntrega(models.Model):
    id = models.BooleanField(primary_key=True, default=uuid.uuid4,editable=False)
    version = models.BigIntegerField()
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING)
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

    class Meta:
        managed = False
        db_table = 'direccion_entrega'