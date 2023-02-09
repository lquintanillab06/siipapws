from django.db import models
import uuid

class PreciosPorCliente(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    version = models.BigIntegerField()
    descuento = models.DecimalField(max_digits=19, decimal_places=2)
    activo = models.BooleanField(default=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    cliente_id = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'precios_por_cliente'