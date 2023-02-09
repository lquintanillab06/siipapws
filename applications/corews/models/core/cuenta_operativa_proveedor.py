from django.db import models

from .proveedor import  Proveedor

class CuentaOperativaProveedor(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    cuenta_operativa = models.CharField(max_length=255)
    proveedor = models.ForeignKey(Proveedor, models.DO_NOTHING)
    tipo = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cuenta_operativa_proveedor'