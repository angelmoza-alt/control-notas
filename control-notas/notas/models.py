from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Estudiante(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True)
    foto = models.ImageField(upload_to='estudiantes/', blank=True, null=True)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Evaluacion(models.Model):
    estudiante = models.ForeignKey(
        Estudiante, on_delete=models.CASCADE, related_name='evaluaciones'
    )
    curso = models.CharField(max_length=200)
    nota = models.DecimalField(
        max_digits=4, decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(20)]
    )
    fecha = models.DateField()

    class Meta:
        ordering = ['-fecha']
        verbose_name_plural = 'Evaluaciones'

    def __str__(self):
        return f'{self.curso} - {self.estudiante.nombre} ({self.nota})'
