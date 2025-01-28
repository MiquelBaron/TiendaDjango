from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myshop/', include('myshop.urls')),  # Ruta para productos
    path('', lambda request: redirect('login')),  # Redirige a login si no hay URL raíz definida
    path('accounts/', include('accounts.urls'))  # Ruta para la aplicación de cuentas
]
