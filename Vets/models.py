from django.db import models

# Create your models here.

class AnimalMascota(models.Model):
    animal = models.CharField(max_length=20, unique=True)

class Raza(models.Model):
    raza = models.CharField(max_length=20, unique=True)
    animal = models.ForeignKey(AnimalMascota, on_delete=models.CASCADE)

class Mascota(models.Model):
    animal = models.ForeignKey(AnimalMascota, on_delete=models.CASCADE)
    duenio = models.CharField(max_length=10)
    raza = models.ForeignKey(Raza, on_delete=models.SET_NULL, null=True)
    info_extra = models.TextField(blank=True, null=True)
    fecha_de_nacimiento = models.DateField()

class Cita(models.Model):
    usuario = models.CharField(max_length=10)
    fecha_hora = models.DateTimeField()

class HistorialCita(models.Model):
    desc_cita = models.TextField()
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    cita = models.ForeignKey(Cita, on_delete=models.CASCADE)

class Vacuna(models.Model):
    nombre_vacuna = models.CharField(max_length=40, unique=True)

class Vacunacion(models.Model):
    tipo_vacuna = models.ForeignKey(Vacuna, on_delete=models.CASCADE)
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)