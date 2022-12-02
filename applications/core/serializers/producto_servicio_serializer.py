from rest_framework import serializers

from ..models import ProductoServicio


class ProductoServicioSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductoServicio
        fields = '__all__'