from rest_framework import serializers

from ..models import DescuentoPorVolumen


class DescuentoPorVolumenSerializer(serializers.ModelSerializer):

    class Meta:
        model = DescuentoPorVolumen
        fields = '__all__'