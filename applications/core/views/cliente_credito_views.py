
from email import message
from django.shortcuts import render

from rest_framework.generics import (ListAPIView, 
                                    CreateAPIView, 
                                    RetrieveAPIView, 
                                    DestroyAPIView, 
                                    UpdateAPIView,
                                    RetrieveUpdateAPIView,
                                    RetrieveUpdateDestroyAPIView)

from ..models import ClienteCredito
from ..serializers import ClienteCreditoSerializer


class ClienteCreditoList(ListAPIView):
    queryset = ClienteCredito.objects.all()
    serializer_class = ClienteCreditoSerializer

class ClienteCreditoCreate(CreateAPIView):
    serializer_class = ClienteCreditoSerializer

class ClienteCreditoRetrieve(RetrieveAPIView):
    serializer_class = ClienteCreditoSerializer
    queryset = ClienteCredito.objects.filter()

class ClienteCreditoDelete(DestroyAPIView):
    serializer_class = ClienteCreditoSerializer
    queryset = ClienteCredito.objects.filter()

class ClienteCreditoUpdate(UpdateAPIView):
    serializer_class = ClienteCreditoSerializer
    queryset = ClienteCredito.objects.filter()

class ClienteCreditoGetUpdate(RetrieveUpdateAPIView):
    serializer_class = ClienteCreditoSerializer
    queryset = ClienteCredito.objects.filter()

class ClienteCreditoGetUpdateDelete(RetrieveUpdateDestroyAPIView):
    serializer_class = ClienteCreditoSerializer
    queryset = ClienteCredito.objects.filter()

