from django.db import models
import uuid
from .proveedor import Proveedor

class FacturistaDeEmbarque(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable= False)
    version = models.BigIntegerField()  
    nombre = models.CharField(max_length=255)
    proveedor = models.ForeignKey(Proveedor, models.DO_NOTHING)
    rfc = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    descuent_en_prestamo = models.DecimalField(max_digits=19, decimal_places=2)
    clave = models.IntegerField(blank=True, null=True)
    orden = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    update_user = models.CharField(max_length=255, blank=True, null=True)


    class Meta:
        managed = True
        db_table = 'facturista_de_embarque'