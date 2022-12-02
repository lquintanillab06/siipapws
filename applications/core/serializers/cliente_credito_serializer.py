from rest_framework import serializers

from ..models import ClienteCredito


class ClienteCreditoSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(required = False)
    class Meta:
        model = ClienteCredito
        fields = "__all__"


