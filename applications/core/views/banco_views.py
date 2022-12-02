
from django.shortcuts import render

from rest_framework.generics import (ListAPIView, 
                                    CreateAPIView, 
                                    RetrieveAPIView, 
                                    DestroyAPIView, 
                                    UpdateAPIView,
                                    RetrieveUpdateAPIView,
                                    RetrieveUpdateDestroyAPIView)

from ..models import Banco
from ..serializers import BancoSerializer


class BancoList(ListAPIView):
    queryset = Banco.objects.all()
    serializer_class = BancoSerializer

class BancoCreate(CreateAPIView):
    serializer_class = BancoSerializer

class BancoRetrieve(RetrieveAPIView):
    serializer_class = BancoSerializer
    queryset = Banco.objects.filter()

class BancoDelete(DestroyAPIView):
    serializer_class = BancoSerializer
    queryset = Banco.objects.filter()

class BancoUpdate(UpdateAPIView):
    serializer_class = BancoSerializer
    queryset = Banco.objects.filter()

class BancoGetUpdate(RetrieveUpdateAPIView):
    serializer_class = BancoSerializer
    queryset = Banco.objects.filter()

class BancoGetUpdateDelete(RetrieveUpdateDestroyAPIView):
    serializer_class = BancoSerializer
    queryset = Banco.objects.filter()

