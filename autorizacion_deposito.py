from django.db import models
import uuid



class AutorizacionDeDeposito(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    fecha = models.DateTimeField()
    comentario = models.CharField(max_length=255, blank=True, null=True)
    uid = models.CharField(max_length=255)
    create_user = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'autorizacion_de_deposito'