from email.policy import default
from django.db import models
import uuid


class Chofer(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable= False)
    version = models.BigIntegerField()
    celular = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.CharField(max_length=255, blank=True, null=True)
    last_updated_by = models.CharField(max_length=255, blank=True, null=True)
    mail = models.CharField(max_length=255, blank=True, null=True)
    nombre = models.CharField(max_length=255)
    rfc = models.CharField(max_length=255, blank=True, null=True)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    activo = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'chofer'