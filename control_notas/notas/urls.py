from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # Estudiantes
    path('estudiantes/', views.estudiante_list, name='estudiante_list'),
    path('estudiantes/nuevo/', views.estudiante_create, name='estudiante_create'),
    path('estudiantes/<int:pk>/', views.estudiante_detail, name='estudiante_detail'),
    path('estudiantes/<int:pk>/editar/', views.estudiante_update, name='estudiante_update'),
    path('estudiantes/<int:pk>/eliminar/', views.estudiante_delete, name='estudiante_delete'),
    # Evaluaciones
    path('evaluaciones/', views.evaluacion_list, name='evaluacion_list'),
    path('evaluaciones/nueva/', views.evaluacion_create, name='evaluacion_create'),
    path('evaluaciones/<int:pk>/', views.evaluacion_detail, name='evaluacion_detail'),
    path('evaluaciones/<int:pk>/editar/', views.evaluacion_update, name='evaluacion_update'),
    path('evaluaciones/<int:pk>/eliminar/', views.evaluacion_delete, name='evaluacion_delete'),
]
