
from django.shortcuts import render

from rest_framework.generics import (ListAPIView, 
                                    CreateAPIView, 
                                    RetrieveAPIView, 
                                    DestroyAPIView, 
                                    UpdateAPIView,
                                    RetrieveUpdateAPIView,
                                    RetrieveUpdateDestroyAPIView)

from ..models import Proveedor
from ..serializers import ProveedorSerializer


class ProveedorList(ListAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class ProveedorCreate(CreateAPIView):
    serializer_class = ProveedorSerializer

class ProveedorRetrieve(RetrieveAPIView):
    serializer_class = ProveedorSerializer
    queryset = Proveedor.objects.filter()

class ProveedorDelete(DestroyAPIView):
    serializer_class = ProveedorSerializer
    queryset = Proveedor.objects.filter()

class ProveedorUpdate(UpdateAPIView):
    serializer_class = ProveedorSerializer
    queryset = Proveedor.objects.filter()

class ProveedorGetUpdate(RetrieveUpdateAPIView):
    serializer_class = ProveedorSerializer
    queryset = Proveedor.objects.filter()

class ProveedorGetUpdateDelete(RetrieveUpdateDestroyAPIView):
    serializer_class = ProveedorSerializer
    queryset = Proveedor.objects.filter()
