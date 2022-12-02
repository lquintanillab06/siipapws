
from django.shortcuts import render

from rest_framework.generics import (ListAPIView, 
                                    CreateAPIView, 
                                    RetrieveAPIView, 
                                    DestroyAPIView, 
                                    UpdateAPIView,
                                    RetrieveUpdateAPIView,
                                    RetrieveUpdateDestroyAPIView)

from ..models import Socio
from ..serializers import SocioSerializer


class SocioList(ListAPIView):
    queryset = Socio.objects.all()
    serializer_class = SocioSerializer

class SocioCreate(CreateAPIView):
    serializer_class = SocioSerializer

class SocioRetrieve(RetrieveAPIView):
    serializer_class = SocioSerializer
    queryset = Socio.objects.filter()

class SocioDelete(DestroyAPIView):
    serializer_class = SocioSerializer
    queryset = Socio.objects.filter()

class SocioUpdate(UpdateAPIView):
    serializer_class = SocioSerializer
    queryset = Socio.objects.filter()

class SocioGetUpdate(RetrieveUpdateAPIView):
    serializer_class = SocioSerializer
    queryset = Socio.objects.filter()

class SocioGetUpdateDelete(RetrieveUpdateDestroyAPIView):
    serializer_class = SocioSerializer
    queryset = Socio.objects.filter()

