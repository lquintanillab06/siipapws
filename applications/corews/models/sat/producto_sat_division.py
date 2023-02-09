from django.db import models



class ProductoSatDivision(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    clave = models.CharField(unique=True, max_length=255)
    clave_sat = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'producto_sat_division'