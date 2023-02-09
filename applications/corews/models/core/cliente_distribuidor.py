from django.db import models
import uuid



class ClienteDistribuidor(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    activo = models.BooleanField(default=True)
    clave = models.CharField(max_length=255)
    comentario = models.CharField(max_length=255)
    precio_tonelada = models.DecimalField(max_digits=19, decimal_places=2)
    nombre = models.CharField(max_length=255)
    cliente = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'cliente_distribuidor'