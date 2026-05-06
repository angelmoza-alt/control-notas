# Control de Notas - Sistema de Estudiantes y Evaluaciones

Aplicacion CRUD con Django y MySQL para gestionar estudiantes y sus evaluaciones.

## Modelos

### Estudiante
- `id` - Identificador unico
- `nombre` - Nombre completo
- `email` - Correo electronico (unico)
- `telefono` - Numero de telefono
- `foto` - Imagen del estudiante

### Evaluacion
- `id` - Identificador unico
- `estudiante` - Clave foranea a Estudiante
- `curso` - Nombre del curso
- `nota` - Calificacion (0-20)
- `fecha` - Fecha de la evaluacion

## Funcionalidades
- CRUD completo para Estudiantes y Evaluaciones
- Subida y visualizacion de imagenes
- Interfaz con Bootstrap 5
- Relacion uno a muchos (Estudiante -> Evaluaciones)

## Instalacion local

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Variables de entorno
- `DB_NAME` - Nombre de la base de datos (default: control_notas)
- `DB_USER` - Usuario de MySQL
- `DB_PASSWORD` - Contrasena de MySQL
- `DB_HOST` - Host de MySQL (default: localhost)
- `DB_PORT` - Puerto de MySQL (default: 3306)
- `DATABASE_URL` - URL completa de base de datos (para despliegue)
- `DJANGO_SECRET_KEY` - Clave secreta de Django
- `DEBUG` - Modo debug (default: True)
