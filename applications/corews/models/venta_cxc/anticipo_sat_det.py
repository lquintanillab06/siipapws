from django.db import models
import uuid 

from .anticipo_sat import AnticipoSat

class AnticipoSatDet(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, max_length=255)
    version = models.BigIntegerField()
    anticipo = models.ForeignKey(AnticipoSat, models.DO_NOTHING)
    cobro = models.CharField(max_length=255)
    uuid = models.CharField(max_length=255, blank=True, null=True) 
    egreso_uuid = models.CharField(max_length=255, blank=True, null=True)
    cxc_documento = models.BigIntegerField()
    moneda = models.CharField(max_length=5)
    cxc_tipo = models.CharField(max_length=255)
    egreso_cfdi = models.CharField(max_length=255, blank=True, null=True)
    tipo_de_cambio = models.DecimalField(max_digits=19, decimal_places=6)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    fecha = models.DateField()
    comentario = models.CharField(max_length=255, blank=True, null=True)
    egreso_url = models.CharField(max_length=255, blank=True, null=True)
    cxc = models.CharField(max_length=255)
    importe = models.DecimalField(max_digits=19, decimal_places=2)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'anticipo_sat_det'