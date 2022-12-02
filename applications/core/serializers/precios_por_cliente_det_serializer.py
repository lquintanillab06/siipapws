from rest_framework import serializers

from ..models import PreciosPorClienteDet


class PreciosPorClienteDetSerializer(serializers.ModelSerializer):

    class Meta:
        model = PreciosPorClienteDet
        fields = '__all__'