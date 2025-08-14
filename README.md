# 🩺 Modulo_4_Therapists_bk

Backend Django para la gestión de terapeutas, con API REST y panel web de administración.

---

## 📖 Descripción General

Este proyecto es un sistema backend desarrollado en Django que permite registrar, consultar, editar, eliminar y restaurar terapeutas. Ofrece una API RESTful para integración con frontends y una interfaz web amigable para la gestión manual. Incluye validaciones, manejo de imágenes de perfil y soporte para búsquedas avanzadas.

---

## 🛠️ Tecnologías y Frameworks

- Python 3.x
- Django 5.x
- Django REST Framework
- SQLite3 (por defecto)
- Pillow (para imágenes)
- SweetAlert2 y Axios (en frontend)
- HTML5, CSS3, JavaScript

---

## 📁 Estructura del Proyecto

```plaintext
Modulo_4_Therapists_bk/
├── therapists_project/           # Configuración principal del proyecto Django
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py               # Configuración global (apps, DB, media, etc.)
│   ├── urls.py                   # Rutas principales del proyecto
│   ├── wsgi.py
│   └── [README.md](http://_vscodecontentref_/0)
│
├── therapists/                   # Aplicación principal de gestión de terapeutas
│   ├── __init__.py
│   ├── admin.py                  # Registro de modelos en el admin de Django
│   ├── apps.py
│   ├── models.py                 # Modelo Therapist y campos asociados
│   ├── serializers.py            # Serializadores para la API REST
│   ├── tests.py                  # Pruebas unitarias
│   ├── urls.py                   # Rutas de la app (API REST)
│   ├── views.py                  # Vistas y ViewSets (API y web)
│   ├── migrations/               # Migraciones de base de datos
│   │   ├── __init__.py
│   │   └── 0001_initial.py
│   └── templates/
│       └── therapists_ui.html    # Interfaz web para gestión de terapeutas
│
└── requirements.txt              # Dependencias del proyecto (si aplica)

```
---
## 🔗 Rutas Principales

- **`/api/therapists/`** — Endpoints RESTful para CRUD de terapeutas.  
- **`/therapists/ui/`** — Interfaz web para gestión manual (según configuración de rutas).

---

## 🗂️ Endpoints API Destacados

| Método | Ruta                          | Descripción                | Parámetros               |
|--------|--------------------------------|----------------------------|--------------------------|
| GET    | `/api/therapists/`             | Lista todos los terapeutas | `search` (opcional)      |
| POST   | `/api/therapists/`             | Crea un nuevo terapeuta    | Datos del terapeuta      |
| GET    | `/api/therapists/{id}/`        | Detalle de un terapeuta    | -                        |
| PUT    | `/api/therapists/{id}/`        | Actualiza un terapeuta     | Datos del terapeuta      |
| PATCH  | `/api/therapists/{id}/`        | Actualiza parcialmente     | Campos a modificar       |
| DELETE | `/api/therapists/{id}/`        | Elimina un terapeuta       | -                        |

---
## 🧩 Dependencias

Incluidas en `requirements.txt`:

- Django>=5.2
- djangorestframework
- Pillow
- django-cors-headers

---

## ✅ Checklist de Documentación

- [ ] Estructura de archivos y carpetas  
- [ ] Descripción general y tecnologías  
- [ ] Rutas principales y endpoints  
- [ ] Dependencias principales  

---

## 👨‍💻 Autor

Equipo de desarrollo **Modulo_4_Therapists_bk**
