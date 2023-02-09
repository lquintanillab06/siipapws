from django.db import models
from ..cuenta_contable import CuentaContable


class ProductoSatClase(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    clave = models.CharField(unique=True, max_length=255)
    clave_grupo = models.CharField(max_length=255)
    clave_sat = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    cuenta_contable = models.ForeignKey(CuentaContable, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto_sat_clase'