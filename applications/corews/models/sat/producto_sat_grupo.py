from django.db import models

class ProductoSatGrupo(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    clave_division = models.CharField(max_length=255)
    clave = models.CharField(unique=True, max_length=255)
    clave_sat = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'producto_sat_grupo'