from django.db import models
import uuid

# -- === REVISADA, Sin Uso Para Descontinuar y Elimnar ===

class Operador(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()  
    clave = models.CharField(unique=True, max_length=255)
    nombre = models.CharField(unique=True, max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    class Meta:
        managed = False
        db_table = 'operador'