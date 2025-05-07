# Sistema de Notas y Documentos 📝

## Descripción del Proyecto

El Sistema de Notas y Documentos es una API desarrollada con Django REST Framework que permite gestionar notas, documentos, carpetas y etiquetas. Proporciona funcionalidades CRUD completas para cada entidad y permite compartir notas y documentos.

## Características

* CRUD completo para notas, documentos, carpetas y etiquetas.
* Endpoint para compartir notas y documentos.
* Endpoint para organizar notas y documentos en carpetas.
* Endpoint para buscar por texto completo en notas.

## Tecnologías Utilizadas

* Python 3.10
* Django 5.2.1
* Django REST Framework
* SQLite (base de datos predeterminada)
* Thunder Client/Postman (para pruebas)

## Estructura del Proyecto

```
sistema_notas/
├── sistema_notas/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── gestor/
│   ├── migrations/
│   ├── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── manage.py
└── venv/
```

## Requisitos Previos

* Python 3.10 o superior
* pip
* Django
* Django REST Framework
* Thunder Client o Postman

## Instalación

1. Clona el repositorio:

```
git clone https://github.com/usuario/sistema_notas.git
cd sistema_notas
```

2. Crea y activa el entorno virtual:

```
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. Instala las dependencias:

```
pip install -r requirements.txt
```

4. Realiza las migraciones:

```
python manage.py makemigrations\python manage.py migrate
```

5. Crea un superusuario:

```
python manage.py createsuperuser
```

6. Inicia el servidor:

```
python manage.py runserver
```

## Uso de la API

* La API se puede consumir mediante herramientas como Thunder Client o Postman.

### Endpoints Principales

#### Carpetas

* Crear: `POST /api/carpetas/`
* Listar: `GET /api/carpetas/`
* Actualizar: `PUT /api/carpetas/<id>/`
* Eliminar: `DELETE /api/carpetas/<id>/`

#### Notas

* Crear: `POST /api/notas/`
* Listar: `GET /api/notas/`
* Detalle: `GET /api/notas/<id>/`
* Actualizar: `PUT /api/notas/<id>/`
* Eliminar: `DELETE /api/notas/<id>/`
* Compartir: `GET /api/notas/<id>/compartir/`

## Ejemplos de Respuestas

### Ejemplo de Nota

```json
{
    "id": 1,
    "titulo": "Reunión de Proyecto",
    "contenido": "Discutir los avances del proyecto",
    "carpeta": 1,
    "etiquetas": [1, 2]
}
```

## Pruebas con Thunder Client/Postman

1. Crear una nota:

   * Método: POST
   * URL: `http://127.0.0.1:8000/api/notas/`
   * Cuerpo:

   ```json
   {
       "titulo": "Nota de Prueba",
       "contenido": "Esta es una nota de ejemplo.",
       "carpeta": 1,
       "etiquetas": [1]
   }
   ```
2. Actualizar una nota:

   * Método: PUT
   * URL: `http://127.0.0.1:8000/api/notas/1/`
   * Cuerpo:

   ```json
   {
       "titulo": "Nota Actualizada",
       "contenido": "Contenido modificado."
   }
   ```
3. Eliminar una nota:

   * Método: DELETE
   * URL: `http://127.0.0.1:8000/api/notas/1/`

## Autores y Licencia

Desarrollado por Franco
Licencia: MIT
