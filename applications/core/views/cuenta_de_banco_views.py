
from django.shortcuts import render

from rest_framework.generics import (ListAPIView, 
                                    CreateAPIView, 
                                    RetrieveAPIView, 
                                    DestroyAPIView, 
                                    UpdateAPIView,
                                    RetrieveUpdateAPIView,
                                    RetrieveUpdateDestroyAPIView)

from ..models import CuentaDeBanco
from ..serializers import CuentaDeBancoSerializer


class CuentaDeBancoList(ListAPIView):
    queryset = CuentaDeBanco.objects.all()
    serializer_class = CuentaDeBancoSerializer

class CuentaDeBancoCreate(CreateAPIView):
    serializer_class = CuentaDeBancoSerializer

class CuentaDeBancoRetrieve(RetrieveAPIView):
    serializer_class = CuentaDeBancoSerializer
    queryset = CuentaDeBanco.objects.filter()

class CuentaDeBancoDelete(DestroyAPIView):
    serializer_class = CuentaDeBancoSerializer
    queryset = CuentaDeBanco.objects.filter()

class CuentaDeBancoUpdate(UpdateAPIView):
    serializer_class = CuentaDeBancoSerializer
    queryset = CuentaDeBanco.objects.filter()

class CuentaDeBancoGetUpdate(RetrieveUpdateAPIView):
    serializer_class = CuentaDeBancoSerializer
    queryset = CuentaDeBanco.objects.filter()

class CuentaDeBancoGetUpdateDelete(RetrieveUpdateDestroyAPIView):
    serializer_class = CuentaDeBancoSerializer
    queryset = CuentaDeBanco.objects.filter()

