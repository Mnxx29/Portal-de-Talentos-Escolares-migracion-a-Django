from django.db import models

class Campus(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Campus"


class Postulacion(models.Model):

    AREA_CHOICES = [
        ('musica', 'Música'),
        ('deportes', 'Deportes'),
    ]

    rut          = models.CharField(primary_key=True, max_length=12)
    nombre       = models.CharField(max_length=50)
    apellido     = models.CharField(max_length=50)
    email        = models.EmailField(unique=True, max_length=100)
    telefono     = models.CharField(max_length=20)
    campus       = models.ForeignKey('Campus', on_delete=models.CASCADE, db_column='idCampus')
    area_interes = models.CharField(max_length=10, choices=AREA_CHOICES)
    especialidad = models.CharField(max_length=100)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.nombre) + " " + str(self.apellido)

    class Meta:
        verbose_name_plural = "Postulaciones"
