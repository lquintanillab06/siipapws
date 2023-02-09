from django.db import models
import uuid

from .sat_econta_empresa import SatEcontaEmpresa


class SatEcontaCatalogo(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    version = models.BigIntegerField()
    version_sat = models.CharField(max_length=255)
    empresa = models.ForeignKey(SatEcontaEmpresa, models.DO_NOTHING)
    emisor = models.CharField(max_length=255)
    acuse_url = models.CharField(max_length=255, blank=True, null=True)
    ejercicio = models.IntegerField()
    rfc = models.CharField(max_length=255)
    xml_url = models.CharField(max_length=255)
    file_name = models.CharField(max_length=255)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    mes = models.IntegerField()
    create_user = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    last_updated = models.DateTimeField(auto_now=True,null=True)

    class Meta:
        managed = False
        db_table = 'sat_econta_catalogo'