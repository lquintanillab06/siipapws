from django.db import models
import uuid


class Folio(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable= False)
    version = models.BigIntegerField()
    entidad = models.CharField(max_length=30)
    folio = models.BigIntegerField()
    serie = models.CharField(max_length=20)