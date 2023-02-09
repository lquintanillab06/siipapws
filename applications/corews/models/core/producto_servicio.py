from django.db import models

from .cuenta_contable import CuentaContable
from .sat.producto_sat_clase import ProductoSatClase

class ProductoServicio(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    clasificacion = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    inversion = models.BooleanField(default= True)
    cuenta_contable = models.ForeignKey(CuentaContable, models.DO_NOTHING)
    cuenta_contable_0 = models.CharField(db_column='cuenta_contable', max_length=255)  # Field renamed because of name conflict.
    clase = models.ForeignKey(ProductoSatClase, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto_servicio'