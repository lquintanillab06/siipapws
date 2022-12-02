from rest_framework import serializers

from ..models import Cliente
from .cliente_credito_serializer import ClienteCreditoSerializer



class ClienteSerializer(serializers.ModelSerializer):


    class Meta:
        model = Cliente
        fields = ['id','version','activo','cheque_devuelto','clave','foliorfc','forma_de_pago','juridico','nombre',
                'permite_cheque','rfc','sw2','direccion_calle','direccion_codigo_postal','direccion_colonia','direccion_estado',
                 'direccion_latitud','direccion_longitud','direccion_municipio','direccion_numero_exterior','direccion_numero_interior',
                 'direccion_pais','email','razon_social','regimen_fiscal','sucursal']

        #depth = 1

    