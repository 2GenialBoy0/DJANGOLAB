from django.urls import path
from . import views

urlpatterns = [
    # Página de inicio
    path('', views.home, name='home'),

    # URLs para Proyectos
    path('proyectos/', views.lista_proyectos, name='lista_proyectos'),
    path('proyectos/agregar/', views.agregar_proyecto, name='agregar_proyecto'),
    path('proyectos/editar/<int:id>/', views.editar_proyecto, name='editar_proyecto'),
    path('proyectos/eliminar/<int:id>/', views.eliminar_proyecto, name='eliminar_proyecto'),

    # URLs para Herramientas
    path('herramientas/', views.lista_herramientas, name='lista_herramientas'),
    path('herramientas/agregar/', views.agregar_herramienta, name='agregar_herramienta'),
    path('herramientas/eliminar/<int:id>/', views.eliminar_herramienta, name='eliminar_herramienta'),
]
