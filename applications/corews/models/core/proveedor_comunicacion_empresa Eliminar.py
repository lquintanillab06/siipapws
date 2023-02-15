from django.db import models
import uuid

from .proveedor import Proveedor

# === REVISADA, Sin Uso Para Descontinuar y Elimnar ===

class ProveedorComunicacionEmpresa(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4 , editable=False)
    version = models.BigIntegerField()
    activo = models.BooleanField(default=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    proveedor = models.ForeignKey(Proveedor, models.DO_NOTHING)
    sw2 = models.BigIntegerField()
    tipo = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'proveedor_comunicacion_empresa'