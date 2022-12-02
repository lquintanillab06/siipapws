
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import (ListAPIView, 
                                    CreateAPIView, 
                                    RetrieveAPIView, 
                                    DestroyAPIView, 
                                    UpdateAPIView,
                                    RetrieveUpdateAPIView,
                                    RetrieveUpdateDestroyAPIView)

from ..serializers.cliente_credito_serializer import ClienteCreditoSerializer

from ..models import Cliente
from ..serializers import ClienteSerializer


class ClienteList(ListAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteCreate(CreateAPIView):
    serializer_class = ClienteSerializer

class ClienteRetrieve(RetrieveAPIView):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.filter()

class ClienteDelete(DestroyAPIView):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.filter()

class ClienteUpdate(UpdateAPIView):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.filter()

class ClienteGetUpdate(RetrieveUpdateAPIView):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.filter()

class ClienteGetUpdateDelete(RetrieveUpdateDestroyAPIView):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.filter()



@api_view(['POST'])
def add_to_cliente_cliente_credito(request,cliente):
    print(request.data)

    cliente = Cliente.objects.get(id = cliente)
    print(cliente)
    print(request.data)
    credito_serializer = ClienteCreditoSerializer(request.data)

    return Response({"message":"Helloooo!"})