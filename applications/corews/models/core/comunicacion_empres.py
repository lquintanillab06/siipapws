from django.db import models
import uuid

from .cliente import Cliente

# REVISDA, se quito sw2

class ComunicacionEmpresa(models.Model):
    id = models.UUIDField(primary_key=True,default= uuid.uuid4, editable=False)
    version = models.BigIntegerField()
    activo = models.BooleanField(default=True)
    tipo = models.CharField(max_length=4)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING)
    cfdi = models.BooleanField(default=True)
    validado = models.TextField(blank=True, null=True)  # This field type is a guess.
    sucursal_updated = models.CharField(max_length=255, blank=True, null=True)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    sucursal_created = models.CharField(max_length=255, blank=True, null=True)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True,null= True)

    class Meta:
        managed = False
        db_table = 'comunicacion_empresa'