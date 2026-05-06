from django import forms
from .models import Estudiante, Evaluacion


class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'email', 'telefono', 'foto']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class EvaluacionForm(forms.ModelForm):
    class Meta:
        model = Evaluacion
        fields = ['estudiante', 'curso', 'nota', 'fecha']
        widgets = {
            'estudiante': forms.Select(attrs={'class': 'form-control'}),
            'curso': forms.TextInput(attrs={'class': 'form-control'}),
            'nota': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0', 'max': '20'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
