import openpyxl
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleado
from .forms import EmpleadoForm
from django.contrib import messages

def inicio(request):
    return render(request, 'inicio.html')

def lista_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'lista_empleados.html', {'empleados': empleados})

def agregar_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Empleado agregado con éxito.')
            return redirect('lista_empleados')
        else:
            for field, errors in form.errors.items():
                print(f'Error en {field}: {errors}')
            messages.error(request, 'Por favor corrija los errores del formulario.')
    else:
        form = EmpleadoForm()

    return render(request, 'agregar_empleado.html', {'form': form, 'editar': False})

def editar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            messages.success(request, 'Empleado actualizado con éxito.')
            return redirect('lista_empleados')
        else:
            for field, errors in form.errors.items():
                print(f'Error en {field}: {errors}')
            messages.error(request, 'Por favor corrija los errores del formulario.')
    else:
        form = EmpleadoForm(instance=empleado)

    return render(request, 'editar_empleado.html', {'form': form, 'empleado': empleado})

def eliminar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, pk=empleado_id)
    empleado.delete()
    messages.success(request, 'Empleado eliminado con éxito.')
    return redirect('lista_empleados')

def generar_reporte_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'reporte_empleados.html', {'empleados': empleados})

def exportar_reporte_empleados(request):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Reporte de Empleados"

    columnas = [
        'Nombre', 'Apellido Paterno', 'Apellido Materno', 'Género', 'RUT',
        'Fecha de Nacimiento', 'Fecha de Ingreso', 'Fecha de Término de Contrato',
        'Años de Servicio', 'Grado', 'Condición', 'Escalón', 'Cargo',
        'Dirección de Pertenencia', 'Título Profesional', 'Situación Actual',
        'Fecha de Término', 'Observaciones', 'Dirección', 'Situación Discapacidad', 'Etnia'
    ]
    ws.append(columnas)

    empleados = Empleado.objects.all()
    for empleado in empleados:
        fila = [
            empleado.nombre, 
            empleado.apellido_paterno, 
            empleado.apellido_materno,
            empleado.get_genero_display(), 
            empleado.rut, 
            empleado.fecha_nacimiento.strftime('%d/%m/%Y') if empleado.fecha_nacimiento else '',
            empleado.fecha_ingreso.strftime('%d/%m/%Y') if empleado.fecha_ingreso else '',
            empleado.fecha_termino_contrata.strftime('%d/%m/%Y') if empleado.fecha_termino_contrata else '',
            empleado.anios_servicio, 
            empleado.grado, 
            empleado.get_condicion_display(),
            empleado.escalon, 
            empleado.cargo, 
            empleado.direccion_pertenencia,
            empleado.titulo_profesional, 
            empleado.get_situacion_actual_display(),
            empleado.fecha_termino.strftime('%d/%m/%Y') if empleado.fecha_termino else '',
            empleado.observaciones,
            empleado.direccion if empleado.direccion else '',  # Dirección
            empleado.get_situacion_discapacidad_display() if empleado.situacion_discapacidad else '',  # Discapacidad
            empleado.get_etnia_display() if empleado.etnia else '',  # Etnia
        ]
        ws.append(fila)

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=reporte_empleados.xlsx'
    wb.save(response)
    return response
