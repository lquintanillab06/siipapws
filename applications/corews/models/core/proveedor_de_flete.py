from django.db import models
import uuid

class ProveedorDeFlete(models.Model):
    id = models.UUIDField(primary_key=True,default= uuid.uuid4,editable=False)
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'proveedor_de_flete'