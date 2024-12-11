from django import forms
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = [
            'nombre', 'apellido_paterno', 'apellido_materno', 'genero', 'rut', 'telefono', 'correo_electronico',
            'fecha_nacimiento', 'fecha_ingreso', 'fecha_termino_contrata', 'anios_servicio', 'grado', 
            'condicion', 'tipo_honorario', 
            'item_presupuestario', 'cta_administracion_fondos',
            'escalon', 'cargo', 'direccion_pertenencia', 'jefatura',
            'titulo_profesional',
            'situacion_actual', 'fecha_termino', 'observaciones',
            'direccion', 'situacion_discapacidad', 'etnia',
        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_paterno': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_materno': forms.TextInput(attrs={'class': 'form-control'}),
            'genero': forms.Select(choices=Empleado.GENERO_CHOICES, attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'correo_electronico': forms.EmailInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_ingreso': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_termino_contrata': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'anios_servicio': forms.TextInput(attrs={'class': 'form-control'}),
            'grado': forms.NumberInput(attrs={'class': 'form-control'}),
            'condicion': forms.Select(choices=Empleado.CONDICION_CHOICES, attrs={'class': 'form-control'}),
            'tipo_honorario': forms.Select(choices=Empleado.TIPO_HONORARIO_CHOICES, attrs={'class': 'form-control'}),
            'item_presupuestario': forms.TextInput(attrs={'class': 'form-control'}),
            'cta_administracion_fondos': forms.TextInput(attrs={'class': 'form-control'}),
            'escalon': forms.TextInput(attrs={'class': 'form-control'}),
            'cargo': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion_pertenencia': forms.TextInput(attrs={'class': 'form-control'}),
            'jefatura': forms.TextInput(attrs={'class': 'form-control'}),
            'titulo_profesional': forms.TextInput(attrs={'class': 'form-control'}),
            'situacion_actual': forms.Select(choices=Empleado.SITUACION_CHOICES, attrs={'class': 'form-control'}),
            'fecha_termino': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'situacion_discapacidad': forms.Select(choices=Empleado.DISCAPACIDAD_CHOICES, attrs={'class': 'form-control'}),
            'etnia': forms.Select(choices=Empleado.ETNIA_CHOICES, attrs={'class': 'form-control'}),
        }