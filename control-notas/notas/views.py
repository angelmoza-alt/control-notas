from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Estudiante, Evaluacion
from .forms import EstudianteForm, EvaluacionForm


def home(request):
    total_estudiantes = Estudiante.objects.count()
    total_evaluaciones = Evaluacion.objects.count()
    ultimas_evaluaciones = Evaluacion.objects.select_related('estudiante')[:5]
    return render(request, 'notas/home.html', {
        'total_estudiantes': total_estudiantes,
        'total_evaluaciones': total_evaluaciones,
        'ultimas_evaluaciones': ultimas_evaluaciones,
    })


# --- Estudiante CRUD ---

def estudiante_list(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'notas/estudiante_list.html', {'estudiantes': estudiantes})


def estudiante_detail(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    evaluaciones = estudiante.evaluaciones.all()
    return render(request, 'notas/estudiante_detail.html', {
        'estudiante': estudiante,
        'evaluaciones': evaluaciones,
    })


def estudiante_create(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Estudiante creado exitosamente.')
            return redirect('estudiante_list')
    else:
        form = EstudianteForm()
    return render(request, 'notas/estudiante_form.html', {'form': form, 'title': 'Nuevo Estudiante'})


def estudiante_update(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == 'POST':
        form = EstudianteForm(request.POST, request.FILES, instance=estudiante)
        if form.is_valid():
            form.save()
            messages.success(request, 'Estudiante actualizado exitosamente.')
            return redirect('estudiante_list')
    else:
        form = EstudianteForm(instance=estudiante)
    return render(request, 'notas/estudiante_form.html', {'form': form, 'title': 'Editar Estudiante'})


def estudiante_delete(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == 'POST':
        estudiante.delete()
        messages.success(request, 'Estudiante eliminado exitosamente.')
        return redirect('estudiante_list')
    return render(request, 'notas/estudiante_confirm_delete.html', {'estudiante': estudiante})


# --- Evaluacion CRUD ---

def evaluacion_list(request):
    evaluaciones = Evaluacion.objects.select_related('estudiante').all()
    return render(request, 'notas/evaluacion_list.html', {'evaluaciones': evaluaciones})


def evaluacion_detail(request, pk):
    evaluacion = get_object_or_404(Evaluacion.objects.select_related('estudiante'), pk=pk)
    return render(request, 'notas/evaluacion_detail.html', {'evaluacion': evaluacion})


def evaluacion_create(request):
    if request.method == 'POST':
        form = EvaluacionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Evaluacion creada exitosamente.')
            return redirect('evaluacion_list')
    else:
        form = EvaluacionForm()
    return render(request, 'notas/evaluacion_form.html', {'form': form, 'title': 'Nueva Evaluacion'})


def evaluacion_update(request, pk):
    evaluacion = get_object_or_404(Evaluacion, pk=pk)
    if request.method == 'POST':
        form = EvaluacionForm(request.POST, instance=evaluacion)
        if form.is_valid():
            form.save()
            messages.success(request, 'Evaluacion actualizada exitosamente.')
            return redirect('evaluacion_list')
    else:
        form = EvaluacionForm(instance=evaluacion)
    return render(request, 'notas/evaluacion_form.html', {'form': form, 'title': 'Editar Evaluacion'})


def evaluacion_delete(request, pk):
    evaluacion = get_object_or_404(Evaluacion, pk=pk)
    if request.method == 'POST':
        evaluacion.delete()
        messages.success(request, 'Evaluacion eliminada exitosamente.')
        return redirect('evaluacion_list')
    return render(request, 'notas/evaluacion_confirm_delete.html', {'evaluacion': evaluacion})
