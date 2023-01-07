from rest_framework import serializers

from .models import MarcaPruebas, PerfilPruebas, UsuarioPruebas
from .pojos import Comentario


class MarcaPruebasSerializer(serializers.ModelSerializer):

    class Meta:
        model = MarcaPruebas
        fields = '__all__'

class MarcaPruebasSerializerPartial(serializers.ModelSerializer):
    
    class Meta:
        model = MarcaPruebas
        fields = ['id','activa','marca']


class ComentarioSerializer(serializers.Serializer):

    nombre= serializers.CharField()
    texto = serializers.CharField(max_length = 200)

    def validate_nombre(self,value):
        print("Validando el nombre")
        if value == 'Luis Quintanilla':
            print("Error")
            #raise serializers.ValidationError("Error en el nombre")
        return value

    def validate(self, data):
        print("Validando el objeto completo")
        return data

    def create(self, validated_data):
        return Comentario(**validated_data)

    def update(self, instance, validated_data):
        instance.texto = validated_data['texto']
        return instance



class PerfilPruebasSerializer(serializers.ModelSerializer):
    class Meta:
        model =  PerfilPruebas
        fields= ['username','nip']


class UsuarioPruebasSerializer(serializers.ModelSerializer):
    perfil = PerfilPruebasSerializer()
    class Meta:
        model = UsuarioPruebas
        fields= ['nombre','email','perfil']

    def create(self, validated_data):
        print("Ejecutando el create con: ", validated_data)
        perfil_data = validated_data.pop('perfil')
        print("*"*100)
        print(perfil_data)
        print(validated_data)
        print("*"*100)
        usuario = UsuarioPruebas.objects.create(**validated_data)
        PerfilPruebas.objects.create(usuario = usuario, **perfil_data)
        return usuario 
