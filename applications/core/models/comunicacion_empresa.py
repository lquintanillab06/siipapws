from django.db import models
import uuid

from .cliente import Cliente

class ComunicacionEmpresa(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable= False)
    version = models.BigIntegerField()
    activo = models.BooleanField(default= True) 
    tipo = models.CharField(max_length=4)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    sw2 = models.BigIntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING, related_name= 'comunicaciones')
    cfdi = models.BooleanField(default=False)
    validado = models.BooleanField(default= False)  
    sucursal_updated = models.CharField(max_length=255, blank=True, null=True)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    sucursal_created = models.CharField(max_length=255, blank=True, null=True)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    

    class Meta:
        managed = True
        db_table = 'comunicacion_empresa'