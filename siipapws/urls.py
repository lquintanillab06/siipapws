from django.contrib import admin
from django.urls import path, include


 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('applications.authentication.urls')),
    path('',include('applications.core.urls')),
    path('',include('applications.facturacion.urls')),
    path('',include('applications.pruebas.urls')),
]
