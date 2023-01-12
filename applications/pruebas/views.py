from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView,CreateAPIView
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser, FileUploadParser
from rest_framework.permissions import IsAuthenticated
# Create your views here.


from ..core.serializers import ProductoSerializer,BancoSerializer
from ..core.models import Producto, Banco

from .serializers import MarcaPruebasSerializer, MarcaPruebasSerializerPartial, ComentarioSerializer, UsuarioPruebasSerializer
from .models import MarcaPruebas,UsuarioPruebas, PerfilPruebas
from .permisions import IsAdminOrReadOnly
from .pagination import LargeResultsSetPagination,CursorSetPagination

from ..authentication.models import User

from .pojos import Comentario






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
    #pagination_class = LargeResultsSetPagination
    pagination_class = LargeResultsSetPagination
    serializer_class = MarcaPruebasSerializerPartial


class MarcaPruebaViewSet(ViewSet):

    #permission_classes = [IsAuthenticated]
    permission_classes = [IsAdminOrReadOnly]

    queryset = MarcaPruebas.objects.all()

    def list(self, request):
        # url -> http://localhost:8000/api/marcas 'dependiendo del metodo se ejecuta una accion'
        serialized = MarcaPruebasSerializer(self.queryset, many= True)
        #print(datos)

        user = User.objects.get(pk=2)

        print(user)
        print(user.has_perm('pruebas.delete_usuariopruebas'))
        print(user.has_perm('pruebas.add_usuariopruebas'))
        print(user.has_perm('core.add_proveedor'))
        print(user.has_perm('core.add_cliente'))
        print(user.has_perm('pruebas.set_password'))
        #user.set_password('dragon')
        #user.save()
        return Response({'Respuesta': 'Exitoso desde View SET!!!!!!','datos': serialized.data},HTTP_200_OK, content_type='application/json')

        
    def create(self,request):

        print(request.data)
        return Response({'Respuesta': 'Exitoso desde el create del view set!!!!!!','datos': request.data},HTTP_200_OK, content_type='application/json')
    
    def retrieve(self,request, pk = None):
        print(pk)
        return Response({'Respuesta': 'Exitoso desde el retrieve del view set!!!!!!','datos': request.data},HTTP_200_OK, content_type='application/json')

    @action(detail= False, methods = ['GET'])
    def listar(self, request):
        # url -> http://localhost:8000/api/marcas/listar
        return Response({"Respuesta":"Exitoso desde el action "})



class MarcaTestViewSet(ViewSet):
    
    queryset = MarcaPruebas.objects.all()

    def list(self, request):
        # url -> http://localhost:8000/api/marcas 'dependiendo del metodo se ejecuta una accion'
        serialized = MarcaPruebasSerializer(self.queryset, many= True)
        #print(datos)
        return Response({'Respuesta': 'Exitoso desde View SET de Test!!!!!!','datos': serialized.data},HTTP_200_OK, content_type='application/json')



class MarcaModelViewSet(ModelViewSet):
    queryset = MarcaPruebas.objects.all()
    serializer_class = MarcaPruebasSerializer

    @action(detail= False, methods = ['GET'])
    def listar(self, request):
        # url -> http://localhost:8000/api/marcas/listar
        return Response({"Respuesta":"Exitoso desde el action "})


class ViewParser(APIView):

    parser_classes=[FileUploadParser]

    def post(self, request, filename, format=None):
        print(request.data['file'])
        return Response({"Texto": "Prueba de Parser"})

    def put(self, request, filename, format=None):
        print(filename)
        print(request.data)
        file = request.data['file']
        return HttpResponse(file, content_type='application/pdf')


class TestSerializer(APIView):

    def get(self, request):

        datos = request.data
        #print(datos)
        comentario = Comentario(nombre=datos['nombre'],texto= datos['texto'])
        # Serializacion
        datos_serialized = ComentarioSerializer(comentario)
        print("Datos serializados: ",datos_serialized.data)

        # Des serializacion
        ser = ComentarioSerializer(data=datos_serialized.data)
        print(ser.is_valid())
        print("Datos validados: ",ser.validated_data)

        comentario2 = ser.create(ser.validated_data)

        print("Comentario2: ", comentario2.__dict__)

        ser2 = ComentarioSerializer(data={'nombre':'juan','texto': 'texto_actualizado'})
        print(ser2.is_valid())
        comentario2_act = ser2.update(comentario2,ser2.validated_data)
        print("Comentario3: ", comentario2_act.__dict__)
        return Response(datos_serialized.data)


class CreateUsuarioPruebas(CreateAPIView):
    serializer_class = UsuarioPruebasSerializer
    
    ''' def post(self, request):
        print(request.data)
        serializer = UsuarioPruebasSerializer(data = request.data)
        print(serializer.is_valid())
        print(serializer.validated_data['perfil'].__dict__)
        #serializer.save()
        return Response({"Res":"Correcto!!!", "data": request.data}) '''

class VistaConFiltro(ListAPIView):

    queryset = MarcaPruebas.objects.all()
    serializer_class = MarcaPruebasSerializer



