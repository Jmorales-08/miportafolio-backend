# 📦 Backend - Portafolio con Django + JWT

Este proyecto es el backend del portafolio personal desarrollado con **Django** y **Django REST Framework**, utilizando autenticación con **JWT** para proteger endpoints y permitir operaciones CRUD de proyectos.

## 🚀 Características

- API RESTful con Django REST Framework
- Autenticación con JWT (`/api/token/`)
- Endpoints protegidos para crear proyectos
- Serializers, Views y Models organizados por app
- Soporte para frontend en React (CORS habilitado)

## 📂 Estructura del Proyecto

```
miportafolio/
├── manage.py
├── miportafolio/        # Configuración global del proyecto
└── proyectos/           # App principal (CRUD de proyectos)
```

## 🛠️ Instalación local

```bash
git clone https://github.com/tu-usuario/miportafolio-backend.git
cd miportafolio-backend
python -m venv env
source env/bin/activate  # o .\env\Scripts\activate en Windows


## ⚙️ Migraciones y servidor

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## 🔐 Endpoint de autenticación

- `POST /api/token/`: Obtener tokens JWT (`access` y `refresh`)
- `POST /api/token/refresh/`: Refrescar token de acceso
- `GET /api/proyectos/`: Listar proyectos (público)
- `POST /api/proyectos/`: Crear proyecto (requiere token)

## 📌 Requisitos

- Python 3.10+
- Django 4+
- Django REST Framework
- djangorestframework-simplejwt
- django-cors-headers

## 📄 Licencia

Este proyecto es solo para fines educativos y personales. Puedes modificarlo libremente.