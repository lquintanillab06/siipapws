from rest_framework import serializers

from ..models import ComunicacionEmpresa


class ComunicacionEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComunicacionEmpresa
        fields = "__all__"

