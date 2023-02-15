from django.db import models

from .despacho_cobranza import DespachoCobranza

# REVISADA, === Sin Uso Para Descontinuar y Elimnar ==

class DespachoAbogados(models.Model):
    despacho = models.ForeignKey(DespachoDeCobranza, models.DO_NOTHING)
    abogado = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'despacho_abogados'