from rest_framework import serializers

from ..models import PreciosPorCliente


class PreciosPorClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = PreciosPorCliente
        fields = '__all__'