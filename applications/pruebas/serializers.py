from rest_framework import serializers

from .models import MarcaPruebas


class MarcaPruebasSerializer(serializers.ModelSerializer):

    class Meta:
        model = MarcaPruebas
        fields = '__all__'

class MarcaPruebasSerializerPartial(serializers.ModelSerializer):
    
    class Meta:
        model = MarcaPruebas
        fields = ['id','activa','marca']