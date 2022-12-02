
from django.shortcuts import render

from rest_framework.generics import (ListAPIView, 
                                    CreateAPIView, 
                                    RetrieveAPIView, 
                                    DestroyAPIView, 
                                    UpdateAPIView,
                                    RetrieveUpdateAPIView,
                                    RetrieveUpdateDestroyAPIView)

from ..models import PreciosPorClienteDet
from ..serializers import PreciosPorClienteDetSerializer


class PreciosPorClienteDetList(ListAPIView):
    queryset = PreciosPorClienteDet.objects.all()
    serializer_class = PreciosPorClienteDetSerializer

class PreciosPorClienteDetCreate(CreateAPIView):
    serializer_class = PreciosPorClienteDetSerializer

class PreciosPorClienteDetRetrieve(RetrieveAPIView):
    serializer_class = PreciosPorClienteDetSerializer
    queryset = PreciosPorClienteDet.objects.filter()

class PreciosPorClienteDetDelete(DestroyAPIView):
    serializer_class = PreciosPorClienteDetSerializer
    queryset = PreciosPorClienteDet.objects.filter()

class PreciosPorClienteDetUpdate(UpdateAPIView):
    serializer_class = PreciosPorClienteDetSerializer
    queryset = PreciosPorClienteDet.objects.filter()

class PreciosPorClienteDetGetUpdate(RetrieveUpdateAPIView):
    serializer_class = PreciosPorClienteDetSerializer
    queryset = PreciosPorClienteDet.objects.filter()

class PreciosPorClienteDetGetUpdateDelete(RetrieveUpdateDestroyAPIView):
    serializer_class = PreciosPorClienteDetSerializer
    queryset = PreciosPorClienteDet.objects.filter()

