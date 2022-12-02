from django.db import models
import uuid

from .vendedor import Vendedor
from .cliente import Cliente

class Socio(models.Model):
    id = models.UUIDField(primary_key= True, default=uuid.uuid4, editable= False)
    version = models.BigIntegerField()
    clave = models.CharField(max_length=255)
    sw2 = models.BigIntegerField(blank=True, null=True)
    vendedor = models.ForeignKey(Vendedor, models.DO_NOTHING, blank=True, null=True)
    nombre = models.CharField(max_length=255)
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING, null= True)
    comision_cobrador = models.DecimalField(max_digits=19, decimal_places=2)
    comision_vendedor = models.DecimalField(max_digits=19, decimal_places=2)
    direccion = models.CharField(max_length=255)
    direccion_fiscal_numero_exterior = models.CharField(max_length=50, blank=True, null=True)
    direccion_fiscal_numero_interior = models.CharField(max_length=50, blank=True, null=True)
    direccion_fiscal_latitud = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    direccion_fiscal_longitud = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    direccion_fiscal_estado = models.CharField(max_length=255, blank=True, null=True)
    direccion_fiscal_pais = models.CharField(max_length=100, blank=True, null=True)
    direccion_fiscal_calle = models.CharField(max_length=200, blank=True, null=True)
    direccion_fiscal_colonia = models.CharField(max_length=255, blank=True, null=True)
    direccion_fiscal_codigo_postal = models.CharField(max_length=255, blank=True, null=True)
    direccion_fiscal_municipio = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null= True)
    last_updated = models.DateTimeField(auto_now=True, null= True)


    class Meta:
        managed = True
        db_table = 'socio'