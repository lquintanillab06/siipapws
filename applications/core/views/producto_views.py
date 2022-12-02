
from django.shortcuts import render

from rest_framework.generics import (ListAPIView, 
                                    CreateAPIView, 
                                    RetrieveAPIView, 
                                    DestroyAPIView, 
                                    UpdateAPIView,
                                    RetrieveUpdateAPIView,
                                    RetrieveUpdateDestroyAPIView)

from ..models import Producto
from ..serializers import ProductoSerializer


class ProductoList(ListAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoCreate(CreateAPIView):
    serializer_class = ProductoSerializer

class ProductoRetrieve(RetrieveAPIView):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.filter()

class ProductoDelete(DestroyAPIView):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.filter()

class ProductoUpdate(UpdateAPIView):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.filter()

class ProductoGetUpdate(RetrieveUpdateAPIView):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.filter()

class ProductoGetUpdateDelete(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.filter()
