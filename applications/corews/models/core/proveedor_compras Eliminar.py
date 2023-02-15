from django.db import models
import uuid

from .proveedor import Proveedor

# === REVISADA, Sin Uso Para Descontinuar y Elimnar (Proveedor las columnas de esta tabla) ===

class ProveedorCompras(models.Model):
    id = models.UUIDField(primary_key=True,default= uuid.uuid4, editable= False)
    version = models.BigIntegerField()
    cuenta_contable = models.CharField(max_length=255, blank=True, null=True)
    descuentof = models.BigIntegerField()
    diasdf = models.BigIntegerField()
    fecha_revision = models.BooleanField(default=False)
    imprimir_costo = models.BooleanField(default=True)
    plazo = models.BigIntegerField()
    proveedor = models.ForeignKey(Proveedor, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedor_compras'