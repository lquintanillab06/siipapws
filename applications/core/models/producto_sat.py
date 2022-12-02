from django.db import models



class ProductoSat(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    clave_prod_serv = models.CharField(unique=True, max_length=255)
    descripcion = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True, null= True)
    last_updated = models.DateTimeField(auto_now=True, null= True)

    class Meta:
        managed = True
        db_table = 'producto_sat'