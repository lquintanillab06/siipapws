from django.db import models

class DespachoDeCobranza(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    telefono3 = models.CharField(max_length=30, blank=True, null=True)
    activo = models.BooleanField(default=True)  # This field type is a guess.
    telefono2 = models.CharField(max_length=30, blank=True, null=True)
    rfc = models.CharField(max_length=13)
    nombre = models.CharField(unique=True, max_length=255)
    telefono1 = models.CharField(max_length=30, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    last_updated = models.DateTimeField(auto_now=True, null= True)

    class Meta:
        managed = False
        db_table = 'despacho_de_cobranza'