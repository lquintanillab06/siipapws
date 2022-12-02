
from django.shortcuts import render

from rest_framework.generics import (ListAPIView, 
                                    CreateAPIView, 
                                    RetrieveAPIView, 
                                    DestroyAPIView, 
                                    UpdateAPIView,
                                    RetrieveUpdateAPIView,
                                    RetrieveUpdateDestroyAPIView)

from ..models import ProductoServicio
from ..serializers import ProductoServicioSerializer


class ProductoServicioList(ListAPIView):
    queryset = ProductoServicio.objects.all()
    serializer_class = ProductoServicioSerializer

class ProductoServicioCreate(CreateAPIView):
    serializer_class = ProductoServicioSerializer

class ProductoServicioRetrieve(RetrieveAPIView):
    serializer_class = ProductoServicioSerializer
    queryset = ProductoServicio.objects.filter()

class ProductoServicioDelete(DestroyAPIView):
    serializer_class = ProductoServicioSerializer
    queryset = ProductoServicio.objects.filter()

class ProductoServicioUpdate(UpdateAPIView):
    serializer_class = ProductoServicioSerializer
    queryset = ProductoServicio.objects.filter()

class ProductoServicioGetUpdate(RetrieveUpdateAPIView):
    serializer_class = ProductoServicioSerializer
    queryset = ProductoServicio.objects.filter()

class ProductoServicioGetUpdateDelete(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductoServicioSerializer
    queryset = ProductoServicio.objects.filter()

