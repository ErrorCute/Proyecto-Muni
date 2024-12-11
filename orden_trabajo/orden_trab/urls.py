# orden_trab/urls.py
from django.urls import path
from . import views 

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('lista_empleados/', views.lista_empleados, name='lista_empleados'),
    path('agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('editar/<int:id>/', views.editar_empleado, name='editar_empleado'),
    path('eliminar/<int:empleado_id>/', views.eliminar_empleado, name='eliminar_empleado'),
    path('reporte_empleados/', views.generar_reporte_empleados, name='reporte_empleados'),
    path('exportar_reporte_empleados/', views.exportar_reporte_empleados, name='exportar_reporte_empleados'),
    path('eliminar_empleado/<int:id>/', views.eliminar_empleado, name='eliminar_empleado')
]

