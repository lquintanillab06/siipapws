from rest_framework import serializers

from ..models import ListaDePreciosVentaDet


class ListaDePreciosVentaDetSerializer(serializers.ModelSerializer):

    id = serializers.UUIDField(required = False)

    class Meta:
        model = ListaDePreciosVentaDet
        fields = '__all__'
        read_only_fields = ['lista']