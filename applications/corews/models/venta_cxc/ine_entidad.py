from django.db import models
import uuid

from .venta_ine import VentaIne

class IneEntidad(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    version = models.BigIntegerField()
    ambito = models.CharField(max_length=255)
    clave = models.CharField(max_length=255)
    complementoine = models.ForeignKey(VentaIne, models.DO_NOTHING)
    contabilidades = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ine_entidad'