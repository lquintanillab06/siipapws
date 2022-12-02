
from django.shortcuts import render

from rest_framework.generics import (ListAPIView, 
                                    CreateAPIView, 
                                    RetrieveAPIView, 
                                    DestroyAPIView, 
                                    UpdateAPIView,
                                    RetrieveUpdateAPIView,
                                    RetrieveUpdateDestroyAPIView)

from ..models import ComunicacionEmpresa
from ..serializers import ComunicacionEmpresaSerializer


class ComunicacionEmpresaList(ListAPIView):
    queryset = ComunicacionEmpresa.objects.all()
    serializer_class = ComunicacionEmpresaSerializer

class ComunicacionEmpresaCreate(CreateAPIView):
    serializer_class = ComunicacionEmpresaSerializer

class ComunicacionEmpresaRetrieve(RetrieveAPIView):
    serializer_class = ComunicacionEmpresaSerializer
    queryset = ComunicacionEmpresa.objects.filter()

class ComunicacionEmpresaDelete(DestroyAPIView):
    serializer_class = ComunicacionEmpresaSerializer
    queryset = ComunicacionEmpresa.objects.filter()

class ComunicacionEmpresaUpdate(UpdateAPIView):
    serializer_class = ComunicacionEmpresaSerializer
    queryset = ComunicacionEmpresa.objects.filter()

class ComunicacionEmpresaGetUpdate(RetrieveUpdateAPIView):
    serializer_class = ComunicacionEmpresaSerializer
    queryset = ComunicacionEmpresa.objects.filter()

class ComunicacionEmpresaGetUpdateDelete(RetrieveUpdateDestroyAPIView):
    serializer_class = ComunicacionEmpresaSerializer
    queryset = ComunicacionEmpresa.objects.filter()

