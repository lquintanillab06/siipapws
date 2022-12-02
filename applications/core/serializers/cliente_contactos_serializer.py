from rest_framework import serializers

from ..models import ClienteContactos


class ClienteContactosSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClienteContactos
        fields = '__all__'