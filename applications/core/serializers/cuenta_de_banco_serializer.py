from rest_framework import serializers

from ..models import CuentaDeBanco


class CuentaDeBancoSerializer(serializers.ModelSerializer):

    class Meta:
        model = CuentaDeBanco
        fields = '__all__'