
from django.shortcuts import render

from rest_framework.generics import (ListAPIView, 
                                    CreateAPIView, 
                                    RetrieveAPIView, 
                                    DestroyAPIView, 
                                    UpdateAPIView,
                                    RetrieveUpdateAPIView,
                                    RetrieveUpdateDestroyAPIView)

from ..models import Marca
from ..serializers import MarcaSerializer


class MarcaList(ListAPIView):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class MarcaCreate(CreateAPIView):
    serializer_class = MarcaSerializer

class MarcaRetrieve(RetrieveAPIView):
    serializer_class = MarcaSerializer
    queryset = Marca.objects.filter()

class MarcaDelete(DestroyAPIView):
    serializer_class = MarcaSerializer
    queryset = Marca.objects.filter()

class MarcaUpdate(UpdateAPIView):
    serializer_class = MarcaSerializer
    queryset = Marca.objects.filter()

class MarcaGetUpdate(RetrieveUpdateAPIView):
    serializer_class = MarcaSerializer
    queryset = Marca.objects.filter()

class MarcaGetUpdateDelete(RetrieveUpdateDestroyAPIView):
    serializer_class = MarcaSerializer
    queryset = Marca.objects.filter()

