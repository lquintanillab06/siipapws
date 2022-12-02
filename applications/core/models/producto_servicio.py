from django.db import models
import uuid

class ProductoServicio(models.Model):
    id = models.UUIDField(primary_key=True,default= uuid.uuid4, editable= False)
    version = models.BigIntegerField(default= 0)
    cuenta_contable = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'producto_servicio'
