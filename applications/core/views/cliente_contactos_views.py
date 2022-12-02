
from django.shortcuts import render

from rest_framework.generics import (ListAPIView, 
                                    CreateAPIView, 
                                    RetrieveAPIView, 
                                    DestroyAPIView, 
                                    UpdateAPIView,
                                    RetrieveUpdateAPIView,
                                    RetrieveUpdateDestroyAPIView)

from ..models import ClienteContactos
from ..serializers import ClienteContactosSerializer


class ClienteContactosList(ListAPIView):
    queryset = ClienteContactos.objects.all()
    serializer_class = ClienteContactosSerializer

class ClienteContactosCreate(CreateAPIView):
    serializer_class = ClienteContactosSerializer

class ClienteContactosRetrieve(RetrieveAPIView):
    serializer_class = ClienteContactosSerializer
    queryset = ClienteContactos.objects.filter()

class ClienteContactosDelete(DestroyAPIView):
    serializer_class = ClienteContactosSerializer
    queryset = ClienteContactos.objects.filter()

class ClienteContactosUpdate(UpdateAPIView):
    serializer_class = ClienteContactosSerializer
    queryset = ClienteContactos.objects.filter()

class ClienteContactosGetUpdate(RetrieveUpdateAPIView):
    serializer_class = ClienteContactosSerializer
    queryset = ClienteContactos.objects.filter()

class ClienteContactosGetUpdateDelete(RetrieveUpdateDestroyAPIView):
    serializer_class = ClienteContactosSerializer
    queryset = ClienteContactos.objects.filter()

