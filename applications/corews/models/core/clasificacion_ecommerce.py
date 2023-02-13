from django.db import models

# REVISADO, no tiene informacion, uso ECOMMERCE

class ClasificacionEcommerce(models.Model):
    id = models.BigIntegerField(primary_key=True)
    version = models.BigIntegerField(blank=True, null=True)
    uso = models.CharField(max_length=255, blank=True, null=True)
    imagen = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clasificacion_ecommerce'