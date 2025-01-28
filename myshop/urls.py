from django.urls import path
from . import views  # Importa las vistas de la app

urlpatterns = [
    path('home/', views.home, name='home'),  # Página de inicio
    path('list/', views.list, name='list'),  # Vista para mostrar los productos
    path('detalles/<int:id>', views.detalles, name='detalles')  # Vista de detalles de un producto
]
