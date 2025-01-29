from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myshop/', include('myshop.urls')),  # Ruta para productos
    path('', include('login.urls'))  # Ruta para la aplicación de cuentas
]
