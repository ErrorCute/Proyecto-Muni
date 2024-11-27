# Generated by Django 5.0.4 on 2024-11-25 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido_paterno', models.CharField(max_length=100)),
                ('apellido_materno', models.CharField(max_length=100)),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], max_length=1)),
                ('rut', models.CharField(max_length=12, unique=True)),
                ('fecha_nacimiento', models.DateField()),
                ('fecha_ingreso', models.DateField()),
                ('fecha_termino_contrata', models.DateField(blank=True, null=True)),
                ('anios_servicio', models.PositiveIntegerField()),
                ('grado', models.PositiveIntegerField()),
                ('condicion', models.CharField(choices=[('Contrata', 'Contrata'), ('Planta', 'Planta'), ('Honorarios', 'Honorarios')], max_length=20)),
                ('escalon', models.CharField(max_length=50)),
                ('cargo', models.CharField(max_length=100)),
                ('direccion_pertenencia', models.CharField(max_length=100)),
                ('titulo_profesional', models.CharField(max_length=100, null=True)),
                ('situacion_actual', models.CharField(choices=[('Activo(a)', 'Activo(a)'), ('Renuncia', 'Renuncia')], max_length=20)),
                ('fecha_termino', models.DateField(blank=True, null=True)),
                ('observaciones', models.TextField(blank=True)),
            ],
        ),
    ]
