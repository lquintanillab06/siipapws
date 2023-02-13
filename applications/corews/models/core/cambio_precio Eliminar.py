from django.db import models
import uuid

class CambioDePrecio(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable= False)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    fecha_de_aplicacion = models.DateTimeField()
    fecha = models.DateField()
    comentario = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField()
    moneda = models.CharField(max_length=3)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    update_user = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cambio_de_precio'