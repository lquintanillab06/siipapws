from django.db  import models
import uuid

from .proveedor import Proveedor

# === REVISADA, Sin Uso Para Descontinuar y Elimnar ===

class ProveedorContactos(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    version = models.BigIntegerField()
    activo = models.BooleanField(default=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    proveedor = models.ForeignKey(Proveedor, models.DO_NOTHING)
    puesto = models.CharField(max_length=255, blank=True, null=True)
    sw2 = models.BigIntegerField()
    telefono = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedor_contactos'

