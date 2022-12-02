
from urllib import request
from django.shortcuts import render

from rest_framework.generics import (ListAPIView, 
                                    CreateAPIView, 
                                    RetrieveAPIView, 
                                    DestroyAPIView, 
                                    UpdateAPIView,
                                    RetrieveUpdateAPIView,
                                    RetrieveUpdateDestroyAPIView)

from ..models import ListaDePreciosVentaDet
from ..serializers import ListaDePreciosVentaDetSerializer


class ListaDePreciosVentaDetList(ListAPIView):
    queryset = ListaDePreciosVentaDet.objects.all()
    serializer_class = ListaDePreciosVentaDetSerializer

class ListaDePreciosVentaDetCreate(CreateAPIView):
    serializer_class = ListaDePreciosVentaDetSerializer

class ListaDePreciosVentaDetRetrieve(RetrieveAPIView):
    serializer_class = ListaDePreciosVentaDetSerializer
    queryset = ListaDePreciosVentaDet.objects.filter()

class ListaDePreciosVentaDetDelete(DestroyAPIView):
    serializer_class = ListaDePreciosVentaDetSerializer
    queryset = ListaDePreciosVentaDet.objects.filter()

class ListaDePreciosVentaDetUpdate(UpdateAPIView):
    serializer_class = ListaDePreciosVentaDetSerializer
    queryset = ListaDePreciosVentaDet.objects.filter()

class ListaDePreciosVentaDetGetUpdate(RetrieveUpdateAPIView):
    serializer_class = ListaDePreciosVentaDetSerializer
    queryset = ListaDePreciosVentaDet.objects.filter()

class ListaDePreciosVentaDetGetUpdateDelete(RetrieveUpdateDestroyAPIView):
    serializer_class = ListaDePreciosVentaDetSerializer
    queryset = ListaDePreciosVentaDet.objects.filter()

class ListaDePreciosVentaPartidasList(ListAPIView):
    def get_queryset(self):
        #print(self.kwargs['lista'])
        return ListaDePreciosVentaDet.objects.filter(lista_id = self.kwargs['lista'])
    serializer_class = ListaDePreciosVentaDetSerializer

