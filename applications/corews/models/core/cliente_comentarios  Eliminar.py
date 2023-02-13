from django.db import models
import uuid

# REVISADA - Para eliminar no se esta usando desde 2020-05-06

class ClienteComentarios(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable= False)
    comentario = models.CharField(max_length=255)
    activo = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    cliente_id = models.CharField(max_length=255, blank=True, null=True)
    tipo = models.CharField(max_length=255, blank=True, null=True)
    sol_activa = models.CharField(max_length=255, blank=True, null=True)
    sol_bloqueo = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null= True)
    last_updated = models.DateTimeField(auto_now=True, null= True)

    

    class Meta:
        managed = False
        db_table = 'cliente_comentarios'
