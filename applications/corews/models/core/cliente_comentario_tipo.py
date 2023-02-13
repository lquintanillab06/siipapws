from django.db import models
import uuid

# Revisada

class ClienteComentarioTipo(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable= False)
    version = models.BigIntegerField()
    descripcion = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True, null= True)
    last_updated = models.DateTimeField(auto_now=True, null= True)    

    class Meta:
        managed = False
        db_table = 'cliente_comentario_tipo'