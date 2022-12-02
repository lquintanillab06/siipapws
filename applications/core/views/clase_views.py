
from django.shortcuts import render

from rest_framework.generics import (ListAPIView, 
                                    CreateAPIView, 
                                    RetrieveAPIView, 
                                    DestroyAPIView, 
                                    UpdateAPIView,
                                    RetrieveUpdateAPIView,
                                    RetrieveUpdateDestroyAPIView)

from ..models import Clase
from ..serializers import ClaseSerializer


class ClaseList(ListAPIView):
    queryset = Clase.objects.all()
    serializer_class = ClaseSerializer

class ClaseCreate(CreateAPIView):
    serializer_class = ClaseSerializer

class ClaseRetrieve(RetrieveAPIView):
    serializer_class = ClaseSerializer
    queryset = Clase.objects.filter()

class ClaseDelete(DestroyAPIView):
    serializer_class = ClaseSerializer
    queryset = Clase.objects.filter()

class ClaseUpdate(UpdateAPIView):
    serializer_class = ClaseSerializer
    queryset = Clase.objects.filter()

class ClaseGetUpdate(RetrieveUpdateAPIView):
    serializer_class = ClaseSerializer
    queryset = Clase.objects.filter()

class ClaseGetUpdateDelete(RetrieveUpdateDestroyAPIView):
    serializer_class = ClaseSerializer
    queryset = Clase.objects.filter()

