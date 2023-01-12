from django.urls import path

from . import views


urlpatterns = [
    path('api/facturacion', views.Facturacion.as_view(), name='prueba'),
]
