from django.db import models
import uuid

from .venta import Venta

class VentaCancelada(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    version = models.BigIntegerField()
    fecha = models.DateField()
    usuario = models.CharField(max_length=255, blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    venta = models.ForeignKey(Venta, models.DO_NOTHING)
    autorizacion = models.CharField(max_length=255)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'venta_cancelada'