from rest_framework import serializers




from ..models import ListaDePreciosVenta, ListaDePreciosVentaDet
from .lista_de_precios_venta_det_serializer import ListaDePreciosVentaDetSerializer


class ListaDePreciosVentaSerializer(serializers.ModelSerializer):

    partidas = ListaDePreciosVentaDetSerializer(many = True)

    class Meta:
        model = ListaDePreciosVenta
        fields =['id','version','folio','tipo_de_cambio_dolar','sw2','autorizacion','descripcion','inicio','aplicada'
                ,'linea', 'partidas']

    def create(self, validated_data):
        partidas = validated_data.pop('partidas')
        lista = ListaDePreciosVenta.objects.create(**validated_data)
        for partida in partidas:
            ListaDePreciosVentaDet.objects.create(**partida,lista = lista)
        return lista


    def update(self, instance , validated_data):

        partidas = validated_data.pop('partidas')

        instance.version = validated_data.get('version', instance.version)
        instance.folio = validated_data.get('folio', instance.folio)
        instance.tipo_de_cambio_dolar = validated_data.get('tipo_de_cambio_dolar', instance.tipo_de_cambio_dolar)
        instance.sw2 = validated_data.get('sw2', instance.sw2)
        instance.autorizacion = validated_data.get('autorizacion', instance.autorizacion)
        instance.descripcion = validated_data.get('descripcion', instance.descripcion)
        instance.inicio = validated_data.get('inicio', instance.inicio)
        instance.aplicada = validated_data.get('aplicada', instance.aplicada)
        instance.linea = validated_data.get('linea', instance.linea)
        instance.save()

        keep_partidas = []
        
        existing_ids = [c.id for c in instance.partidas]

        for partida in partidas:
            if "id" in partida.keys():
                print(partida)
                if ListaDePreciosVentaDet.objects.filter(id=partida['id']).exists():
                    detalle = ListaDePreciosVentaDet.objects.get(id=partida['id'])
                    detalle.version = partida.get("version",detalle.version)
                    detalle.incremento = partida.get("incremento",detalle.incremento)
                    detalle.factor_credito = partida.get("factor_credito",detalle.factor_credito)
                    detalle.precio_anterior_credito = partida.get("precio_anterior_credito",detalle.precio_anterior_credito)
                    detalle.costo_ultimo = partida.get("costo_ultimo",detalle.costo_ultimo)
                    detalle.precio_anterior_contado = partida.get("precio_anterior_contado",detalle.precio_anterior_contado)
                    detalle.costo = partida.get("costo",detalle.costo)
                    detalle.factor_contado = partida.get("factor_contado",detalle.factor_contado)
                    detalle.precio_credito = partida.get("precio_credito",detalle.precio_credito)
                    detalle.precio_contado = partida.get("precio_contado",detalle.precio_contado)
                    detalle.partidas_idx = partida.get("partidas_idx",detalle.partidas_idx)
                    detalle.proveedor = partida.get("proveedor",detalle.proveedor)
                    detalle.producto = partida.get("producto",detalle.producto)
                    detalle.lista = partida.get("lista",detalle.lista)
                    detalle.save()
                    keep_partidas.append(detalle.id)
                else:
                    continue
            else:
                detalle = ListaDePreciosVentaDet.objects.create(**partida,lista = instance)
                keep_partidas.append(detalle.id)

        for partida in instance.partidas:
            if partida.id not in keep_partidas:
                partida.delete()  
                  

        return instance

 

   