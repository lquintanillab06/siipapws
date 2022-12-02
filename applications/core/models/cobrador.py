from django.db import models
import uuid

class Cobrador(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable= False)
    version = models.BigIntegerField()
    activo = models.BooleanField(default= True) 
    apellido_materno = models.CharField(max_length=255, blank=True, null=True)
    apellido_paterno = models.CharField(max_length=255, blank=True, null=True)
    clave = models.CharField(max_length=255, blank=True, null=True)
    comision = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    curp = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add= True)
    last_updated = models.DateTimeField(auto_now= True)
    nombres = models.CharField(max_length=255, blank=True, null=True)
    rfc = models.CharField(max_length=255, blank=True, null=True)
    sw2 = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cobrador'