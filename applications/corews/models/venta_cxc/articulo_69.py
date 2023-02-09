from django.db import models


class Articulo69(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'articulo69'