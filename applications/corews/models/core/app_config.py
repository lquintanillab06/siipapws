from django.db import models
import uuid

from . import Sucursal

class AppConfig(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    version = models.BigIntegerField()
    cfdi_location = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    sucursal = models.ForeignKey(Sucursal, models.DO_NOTHING)
    envio_de_correos_activo = models.BooleanField(default=True) 

    class Meta:
        managed = True
        db_table = 'app_config'
