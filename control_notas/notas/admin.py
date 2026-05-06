from django.contrib import admin
from .models import Estudiante, Evaluacion


@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono')
    search_fields = ('nombre', 'email')


@admin.register(Evaluacion)
class EvaluacionAdmin(admin.ModelAdmin):
    list_display = ('curso', 'estudiante', 'nota', 'fecha')
    list_filter = ('curso', 'fecha')
    search_fields = ('curso', 'estudiante__nombre')
