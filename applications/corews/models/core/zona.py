from django.db import models
import uuid

# REVISADA, se quito division_zona "Esta tabla se usa en CALLCENTER"
# la columna entidad_id se cambio a " secuencia "

class Zona(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable= False)
    version = models.BigIntegerField()
    area = models.CharField(max_length=255)
    asignacion = models.CharField(max_length=255)
    cp_ini = models.BigIntegerField(blank=True, null=True)    
    cp_fin = models.BigIntegerField(blank=True, null=True)    
    entidad = models.CharField(max_length=255)
    secuencia = models.BigIntegerField()
    sector = models.BigIntegerField()
    sucursal = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zona'