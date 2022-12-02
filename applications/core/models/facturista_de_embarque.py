from django.db import models
import uuid


class FacturistaDeEmbarque(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable= False)
    version = models.BigIntegerField()
    telefono = models.CharField(max_length=255)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    rfc = models.CharField(max_length=13)
    nombre = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'facturista_de_embarque'