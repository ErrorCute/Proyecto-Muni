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
            # Mostrar errores específicos en el log o consola para depuración
            for field, errors in form.errors.items():
                print(f'Error en {field}: {errors}')
            # Pasar los errores a la plantilla para ser mostrados
            messages.error(request, 'Por favor corrija los errores del formulario.')
    else:
        form = EmpleadoForm()

    # Pasar los errores específicos a la plantilla
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
            messages.error(request, 'Por favor corrija los errores del formulario.')
    else:
        form = EmpleadoForm(instance=empleado)

    # Asegúrate de que las fechas se muestren en el formato correcto
    form.fields['fecha_nacimiento'].widget.attrs['value'] = empleado.fecha_nacimiento.strftime('%Y-%m-%d')
    form.fields['fecha_ingreso'].widget.attrs['value'] = empleado.fecha_ingreso.strftime('%Y-%m-%d')
    form.fields['fecha_termino_contrata'].widget.attrs['value'] = empleado.fecha_termino_contrata.strftime('%Y-%m-%d') if empleado.fecha_termino_contrata else ''

    return render(request, 'editar_empleado.html', {'form': form, 'empleado': empleado})



def eliminar_empleado(request, id):
    # Obtener el empleado a eliminar
    empleado = get_object_or_404(Empleado, id=id)

    # Eliminar el empleado
    if request.method == 'POST':
        empleado.delete()
        messages.success(request, 'Empleado eliminado exitosamente.')
        return redirect('lista_empleados')  # Redirigir de nuevo a la lista de empleados

    # Si no es un POST, solo retornar un 404 o redirigir a la lista de empleados
    return redirect('lista_empleados')

def generar_reporte_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'reporte_empleados.html', {'empleados': empleados})

def exportar_reporte_empleados(request):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Reporte de Empleados"

    columnas = [
        'Nombre', 'Apellido Paterno', 'Apellido Materno', 'Género', 'RUT', 'Teléfono',
        'Correo Electrónico', 'Fecha de Nacimiento', 'Fecha de Ingreso',
        'Fecha de Término de Contrato', 'Años de Servicio', 'Grado', 'Condición',
        'Tipo Honorario', 'Item Presupuestario', 'Cuenta Administración de Fondos',
        'Escalón', 'Cargo', 'Dirección de Pertenencia', 'Jefatura', 'Título Profesional',
        'Situación Actual', 'Fecha de Término', 'Observaciones', 'Dirección',
        'Situación de Discapacidad', 'Etnia'
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
            empleado.telefono if empleado.telefono else '',
            empleado.correo_electronico if empleado.correo_electronico else '',
            empleado.fecha_nacimiento.strftime('%d/%m/%Y') if empleado.fecha_nacimiento else '',
            empleado.fecha_ingreso.strftime('%d/%m/%Y') if empleado.fecha_ingreso else '',
            empleado.fecha_termino_contrata.strftime('%d/%m/%Y') if empleado.fecha_termino_contrata else '',
            empleado.anios_servicio if empleado.anios_servicio is not None else '',
            empleado.grado if empleado.grado else '',
            empleado.get_condicion_display() if empleado.condicion else '',
            empleado.tipo_honorario if empleado.tipo_honorario else '',
            empleado.item_presupuestario if empleado.item_presupuestario else '',
            empleado.cta_administracion_fondos if empleado.cta_administracion_fondos else '',
            empleado.escalon if empleado.escalon else '',
            empleado.cargo if empleado.cargo else '',
            empleado.direccion_pertenencia if empleado.direccion_pertenencia else '',
            empleado.jefatura if empleado.jefatura else '',
            empleado.titulo_profesional if empleado.titulo_profesional else '',
            empleado.get_situacion_actual_display() if empleado.situacion_actual else '',
            empleado.fecha_termino.strftime('%d/%m/%Y') if empleado.fecha_termino else '',
            empleado.observaciones if empleado.observaciones else '',
            empleado.direccion if empleado.direccion else '',
            empleado.get_situacion_discapacidad_display() if empleado.situacion_discapacidad else '',
            empleado.get_etnia_display() if empleado.etnia else '',
        ]
        ws.append(fila)

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=reporte_empleados.xlsx'
    wb.save(response)
    return response
