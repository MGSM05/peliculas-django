# 🎬 Catálogo de Películas

Aplicación web desarrollada con **Django 5** que permite gestionar un catálogo de películas con autenticación de usuarios. Cada usuario puede añadir, editar y eliminar sus propias películas, mientras que cualquier visitante puede explorar y buscar en el catálogo.

---

## Características

- **Catálogo público** — listado de todas las películas con búsqueda por título y sinopsis
- **Fichas de película** — vista de detalle con título, género, sinopsis y cartel
- **CRUD completo** — crear, editar y eliminar películas (solo usuarios registrados)
- **Control de permisos** — cada usuario solo puede modificar sus propias películas; los administradores pueden editar cualquiera
- **Autenticación** — registro, inicio y cierre de sesión integrados
- **Subida de imágenes** — cartel opcional para cada película
- **Mensajes de feedback** — confirmaciones y errores tras cada acción

---

## Tecnologías

| Capa | Tecnología |
|------|------------|
| Framework | Django 5.0 |
| Base de datos | SQLite 3 |
| Imágenes | Pillow 11.2 |
| Plantillas | Django Templates + CSS propio |
| Servidor ASGI | Asgiref 3.11 |
| Despliegue | PythonAnywhere |

---

## Estructura del proyecto

```
peliculas-django/
├── peliculas_proyecto/      # Configuración global (settings, urls, wsgi/asgi)
├── peliculas/               # App principal
│   ├── models.py            # Modelo Pelicula
│   ├── views.py             # Vistas basadas en clases (CRUD + búsqueda)
│   ├── urls.py              # Rutas de la app
│   └── migrations/
├── accounts/                # App de autenticación
│   ├── views.py             # Registro de nuevos usuarios
│   └── urls.py
├── templates/
│   ├── base.html            # Plantilla base con navegación
│   ├── peliculas/           # Lista, detalle, formulario, confirmación de borrado
│   └── registration/        # Login y registro
├── static/
│   └── css/estilos.css
├── media/                   # Carteles subidos por los usuarios
├── requirements.txt
└── manage.py
```

---

## Modelo de datos

```python
class Pelicula(models.Model):
    titulo          # CharField — título de la película
    sinopsis        # TextField — descripción
    genero          # CharField — género cinematográfico
    cartel          # ImageField — imagen opcional (upload_to='carteles/')
    fecha_creacion  # DateTimeField — automática al crear
    autor           # ForeignKey(User) — usuario que la añadió
```

---

## Rutas disponibles

| URL | Vista | Descripción |
|-----|-------|-------------|
| `/` | `VistaListaPeliculas` | Catálogo con buscador |
| `/pelicula/<pk>/` | `VistaDetallePelicula` | Ficha completa |
| `/pelicula/nueva/` | `VistaCrearPelicula` | Añadir película *(login requerido)* |
| `/pelicula/<pk>/editar/` | `VistaActualizarPelicula` | Editar *(solo autor o staff)* |
| `/pelicula/<pk>/eliminar/` | `VistaEliminarPelicula` | Eliminar *(solo autor o staff)* |
| `/accounts/signup/` | `SignUpView` | Registro de usuario |
| `/accounts/login/` | — | Inicio de sesión (Django built-in) |
| `/accounts/logout/` | — | Cierre de sesión (Django built-in) |

---

## Instalación y puesta en marcha

```bash
# 1. Clonar el repositorio
git clone https://github.com/tu-usuario/peliculas-django.git
cd peliculas-django

# 2. Crear y activar un entorno virtual
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Aplicar migraciones
python manage.py migrate

# 5. (Opcional) Crear superusuario
python manage.py createsuperuser

# 6. Arrancar el servidor
python manage.py runserver
```

La aplicación quedará disponible en `http://127.0.0.1:8000`.

---

## Requisitos

```
Django==5.0
Pillow==11.2.1
asgiref==3.11.1
sqlparse==0.5.5
tzdata==2025.3
```

---

## Notas de despliegue

El proyecto está configurado para desplegarse en **PythonAnywhere** (`MGSM.pythonanywhere.com`). Antes de pasar a producción recuerda:

- Cambiar `SECRET_KEY` por una clave segura y no compartida
- Establecer `DEBUG = False`
- Configurar `ALLOWED_HOSTS` con el dominio definitivo
- Configurar el almacenamiento de archivos estáticos y media (`collectstatic`)
