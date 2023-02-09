from django.db import models
import uuid

class GrupoDeProducto(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable= False)
    version = models.BigIntegerField()
    activo = models.BooleanField(default= True)  
    descripcion = models.CharField(max_length=255)
    nombre = models.CharField(unique=True, max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'grupo_de_producto'