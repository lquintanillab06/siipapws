
from django.db import models



class ZonasRuteo(models.Model):
    d_codigo = models.CharField(max_length=255, blank=True, null=True)
    d_asentamiento = models.CharField(max_length=255, blank=True, null=True)
    d_tipo_asentamiento = models.CharField(max_length=255, blank=True, null=True)
    d_municipio = models.CharField(max_length=255, blank=True, null=True)
    d_estado = models.CharField(max_length=255, blank=True, null=True)
    d_ciudad = models.CharField(max_length=255, blank=True, null=True)
    d_cp = models.CharField(max_length=255, blank=True, null=True)
    c_estado = models.CharField(max_length=255, blank=True, null=True)
    c_oficina = models.CharField(max_length=255, blank=True, null=True)
    c_cp = models.CharField(max_length=255, blank=True, null=True)
    c_tipo_asentamiento = models.CharField(max_length=255, blank=True, null=True)
    c_municipoioi = models.CharField(max_length=255, blank=True, null=True)
    id_asentamiento_cp = models.CharField(max_length=255, blank=True, null=True)
    d_zona = models.CharField(max_length=255, blank=True, null=True)
    c_cuve_ciudad = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zonas_ruteo'