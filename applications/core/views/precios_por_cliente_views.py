
from django.shortcuts import render

from rest_framework.generics import (ListAPIView, 
                                    CreateAPIView, 
                                    RetrieveAPIView, 
                                    DestroyAPIView, 
                                    UpdateAPIView,
                                    RetrieveUpdateAPIView,
                                    RetrieveUpdateDestroyAPIView)

from ..models import PreciosPorCliente
from ..serializers import PreciosPorClienteSerializer


class PreciosPorClienteList(ListAPIView):
    queryset = PreciosPorCliente.objects.all()
    serializer_class = PreciosPorClienteSerializer

class PreciosPorClienteCreate(CreateAPIView):
    serializer_class = PreciosPorClienteSerializer

class PreciosPorClienteRetrieve(RetrieveAPIView):
    serializer_class = PreciosPorClienteSerializer
    queryset = PreciosPorCliente.objects.filter()

class PreciosPorClienteDelete(DestroyAPIView):
    serializer_class = PreciosPorClienteSerializer
    queryset = PreciosPorCliente.objects.filter()

class PreciosPorClienteUpdate(UpdateAPIView):
    serializer_class = PreciosPorClienteSerializer
    queryset = PreciosPorCliente.objects.filter()

class PreciosPorClienteGetUpdate(RetrieveUpdateAPIView):
    serializer_class = PreciosPorClienteSerializer
    queryset = PreciosPorCliente.objects.filter()

class PreciosPorClienteGetUpdateDelete(RetrieveUpdateDestroyAPIView):
    serializer_class = PreciosPorClienteSerializer
    queryset = PreciosPorCliente.objects.filter()

