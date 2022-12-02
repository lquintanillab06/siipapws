
from django.shortcuts import render

from rest_framework.generics import (ListAPIView, 
                                    CreateAPIView, 
                                    RetrieveAPIView, 
                                    DestroyAPIView, 
                                    UpdateAPIView,
                                    RetrieveUpdateAPIView,
                                    RetrieveUpdateDestroyAPIView)

from ..models import ProveedorProducto
from ..serializers import ProveedorProductoSerializer


class ProveedorProductoList(ListAPIView):
    queryset = ProveedorProducto.objects.all()
    serializer_class = ProveedorProductoSerializer

class ProveedorProductoCreate(CreateAPIView):
    serializer_class = ProveedorProductoSerializer

class ProveedorProductoRetrieve(RetrieveAPIView):
    serializer_class = ProveedorProductoSerializer
    queryset = ProveedorProducto.objects.filter()

class ProveedorProductoDelete(DestroyAPIView):
    serializer_class = ProveedorProductoSerializer
    queryset = ProveedorProducto.objects.filter()

class ProveedorProductoUpdate(UpdateAPIView):
    serializer_class = ProveedorProductoSerializer
    queryset = ProveedorProducto.objects.filter()

class ProveedorProductoGetUpdate(RetrieveUpdateAPIView):
    serializer_class = ProveedorProductoSerializer
    queryset = ProveedorProducto.objects.filter()

class ProveedorProductoGetUpdateDelete(RetrieveUpdateDestroyAPIView):
    serializer_class = ProveedorProductoSerializer
    queryset = ProveedorProducto.objects.filter()
