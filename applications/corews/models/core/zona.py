from django.db import models
import uuid



class Zona(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable= False)
    version = models.BigIntegerField()
    area = models.CharField(max_length=255)
    asignacion = models.CharField(max_length=255)
    cp_fin = models.BigIntegerField(blank=True, null=True)
    cp_ini = models.BigIntegerField(blank=True, null=True)
    division_zona = models.CharField(max_length=255, blank=True, null=True)
    entidad = models.CharField(max_length=255)
    entidad_id = models.BigIntegerField()
    sector = models.BigIntegerField()
    sucursal = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zona'