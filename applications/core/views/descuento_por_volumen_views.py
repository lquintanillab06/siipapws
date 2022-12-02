
from django.shortcuts import render

from rest_framework.generics import (ListAPIView, 
                                    CreateAPIView, 
                                    RetrieveAPIView, 
                                    DestroyAPIView, 
                                    UpdateAPIView,
                                    RetrieveUpdateAPIView,
                                    RetrieveUpdateDestroyAPIView)

from ..models import DescuentoPorVolumen
from ..serializers import DescuentoPorVolumenSerializer


class DescuentoPorVolumenList(ListAPIView):
    queryset = DescuentoPorVolumen.objects.all()
    serializer_class = DescuentoPorVolumenSerializer

class DescuentoPorVolumenCreate(CreateAPIView):
    serializer_class = DescuentoPorVolumenSerializer

class DescuentoPorVolumenRetrieve(RetrieveAPIView):
    serializer_class = DescuentoPorVolumenSerializer
    queryset = DescuentoPorVolumen.objects.filter()

class DescuentoPorVolumenDelete(DestroyAPIView):
    serializer_class = DescuentoPorVolumenSerializer
    queryset = DescuentoPorVolumen.objects.filter()

class DescuentoPorVolumenUpdate(UpdateAPIView):
    serializer_class = DescuentoPorVolumenSerializer
    queryset = DescuentoPorVolumen.objects.filter()

class DescuentoPorVolumenGetUpdate(RetrieveUpdateAPIView):
    serializer_class = DescuentoPorVolumenSerializer
    queryset = DescuentoPorVolumen.objects.filter()

class DescuentoPorVolumenGetUpdateDelete(RetrieveUpdateDestroyAPIView):
    serializer_class = DescuentoPorVolumenSerializer
    queryset = DescuentoPorVolumen.objects.filter()

