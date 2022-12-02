
from django.shortcuts import render

from rest_framework.generics import (ListAPIView, 
                                    CreateAPIView, 
                                    RetrieveAPIView, 
                                    DestroyAPIView, 
                                    UpdateAPIView,
                                    RetrieveUpdateAPIView,
                                    RetrieveUpdateDestroyAPIView)

from ..models import Linea
from ..serializers import LineaSerializer


class LineaList(ListAPIView):
    queryset = Linea.objects.all()
    serializer_class = LineaSerializer

class LineaCreate(CreateAPIView):
    serializer_class = LineaSerializer

class LineaRetrieve(RetrieveAPIView):
    serializer_class = LineaSerializer
    queryset = Linea.objects.filter()

class LineaDelete(DestroyAPIView):
    serializer_class = LineaSerializer
    queryset = Linea.objects.filter()

class LineaUpdate(UpdateAPIView):
    serializer_class = LineaSerializer
    queryset = Linea.objects.filter()

class LineaGetUpdate(RetrieveUpdateAPIView):
    serializer_class = LineaSerializer
    queryset = Linea.objects.filter()

class LineaGetUpdateDelete(RetrieveUpdateDestroyAPIView):
    serializer_class = LineaSerializer
    queryset = Linea.objects.filter()

