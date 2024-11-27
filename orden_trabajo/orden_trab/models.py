from django.db import models

class Empleado(models.Model):
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]
    
    CONDICION_CHOICES = [
        ('Contrata', 'Contrata'),
        ('Planta', 'Planta'),
        ('Honorarios', 'Honorarios'),
        ('Codigo del Trabajo', 'Codigo del Trabajo'),
    ]
    
    SITUACION_CHOICES = [ 
        ('Activo(a)', 'Activo(a)'),
        ('Renuncia', 'Renuncia'),
    ]

    TIPO_HONORARIO_CHOICES = [
        ('Honorario Municipal', 'Honorario Municipal'),
        ('Mixto', 'Mixto'),
        ('Fondos de Terceros', 'Fondos de Terceros'),
    ]

    ETNIA_CHOICES = [
        ('Mapuche', 'Mapuche'),
        ('Aymara', 'Aymara'),
        ('Rapa Nui', 'Rapa Nui'),
        ('Quechua', 'Quechua'),
        ('Colla', 'Colla'),
        ('Atacameño', 'Atacameño'),
        ('Diaguita', 'Diaguita'),
        ('Boricua', 'Boricua'),
        ('Africana', 'Africana'),
        ('Otro', 'Otro'),
        ('No especificada', 'No especificada'),
    ]

    DISCAPACIDAD_CHOICES = [

        ('Si', 'Si'),
        ('No','No'),
    ]
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    rut = models.CharField(max_length=12, unique=True)  # Format: 20.928.257-7
    telefono = models.CharField(max_length=15, null=True, blank=True)  # Ejemplo: +56912345678
    correo_electronico = models.EmailField(max_length=255, null=True, blank=True)

    fecha_nacimiento = models.DateField()  # Format: YYYY-MM-DD
    fecha_ingreso = models.DateField()
    fecha_termino_contrata = models.DateField(null=True, blank=True)
    anios_servicio = models.PositiveIntegerField()
    grado = models.PositiveIntegerField()
    condicion = models.CharField(max_length=20, choices=CONDICION_CHOICES)
    tipo_honorario = models.CharField(max_length=20, choices=TIPO_HONORARIO_CHOICES, null=True, blank=True)

    item_presupuestario = models.CharField(max_length=100, null=True, blank=True)
    cta_administracion_fondos = models.CharField(max_length=100, null=True, blank=True)

    escalon = models.CharField(max_length=50)
    cargo = models.CharField(max_length=100)
    direccion_pertenencia = models.CharField(max_length=100)
    jefatura = models.CharField(max_length=100, null=True, blank=True)

    titulo_profesional = models.CharField(max_length=100, null=True, blank=True)

    situacion_actual = models.CharField(max_length=20, choices=SITUACION_CHOICES)
    fecha_termino = models.DateField(null=True, blank=True)
    observaciones = models.TextField(blank=True)

    direccion = models.CharField(max_length=255, null=True, blank=True)
    situacion_discapacidad = models.CharField(max_length=100, choices=DISCAPACIDAD_CHOICES, null=True, blank=True)
    etnia = models.CharField(max_length=100, choices=ETNIA_CHOICES, null=True, blank=True)


    def __str__(self):
        return f'{self.nombre} {self.apellido_paterno} {self.apellido_materno}'
