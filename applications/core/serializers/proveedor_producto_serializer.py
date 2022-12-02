from rest_framework import serializers

from ..models import ProveedorProducto


class ProveedorProductoSerializer(serializers.ModelSerializer):

    class  Meta:
        model = ProveedorProducto
        fields = "__all__"