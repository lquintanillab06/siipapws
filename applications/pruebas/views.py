from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import ViewSet
# Create your views here.

from ..core.serializers import ProductoSerializer,BancoSerializer
from ..core.models import Producto, Banco

from .serializers import MarcaPruebasSerializer, MarcaPruebasSerializerPartial
from .models import MarcaPruebas






class Prueba1(APIView):

    def get(self, request):
        print("Ejecutando el metodo GET Prueba1 de API View")
        #print(request.query_params['clave'])
        banco = Banco.objects.get(pk='402880fe-603c-7c9c-0103-c8a632568745')
        #banco_serialized = BancoSerializer(data=banco.__dict__)  
        #banco_serialized.is_valid(raise_exception=True)
        banco_serialized = BancoSerializer(banco)  
        diccionario = {"dato1": "dato1"}
        return Response({'Respuesta': 'Exitoso!!!!!!','banco': banco_serialized.data, 'dict': diccionario},HTTP_200_OK)

    def post(self, request):
        print("Ejecutando el metodo POST Prueba1 de API View")
        print(request.data)
        return Response({'Respuesta': 'Exitoso!!!!!!'},HTTP_200_OK, content_type='application/json')

@api_view(['POST'])
def prueba_function(request):
   print(request.query_params)
   print(request.data)
   return Response({'Respuesta': 'Request Correcto !!!', 'data':request.data})


class Listar(ListAPIView):
    
    queryset= Banco.objects.all()
    serializer_class = BancoSerializer


class BancoRetrieve(RetrieveAPIView):
    serializer_class = BancoSerializer
    queryset = Banco.objects.all()


class BancoRetrieve2(RetrieveAPIView):
    
    serializer_class = BancoSerializer
    queryset = None
    def get_queryset(self):
        print(self.request)
        print(self.kwargs)
        print(self.request.query_params)
        print(self.request.data)
        return Banco.objects.all()
    

@api_view(['GET'])
def prueba_banco(request,*args,**kwargs):
   print(request.query_params)
   print(request.data)
   print(args)
   print(kwargs)
   return Response({'Respuesta': 'Request Correcto !!!', 'data':request.data})


class ListarMarcas(ListAPIView):
    queryset = MarcaPruebas.objects.all()
    serializer_class = MarcaPruebasSerializerPartial

class MarcaPruebaViewSet(ViewSet):

    queryset = MarcaPruebas.objects.all()

    def list(self, request):
          queryset = MarcaPruebas.objects.all()


        
    
    