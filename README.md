# Portal de Talentos Escolares (Migración a Django)

Este proyecto corresponde a la **migración a Django** del proyecto original de la página web del **Portal de Talentos Escolares**. Fue desarrollado como parte de los trabajos prácticos para la asignatura de **Programación Web**, dictada por el docente **Francisco Javier Calfun**.

---

## 📋 Descripción del Proyecto

El **Portal de Talentos Escolares** es una plataforma web diseñada para destacar y gestionar las habilidades artísticas y deportivas de los estudiantes de la institución. En esta versión migrada a **Django**, se aprovecha la potencia del patrón MVT (Modelo-Vista-Template) de Django para manejar el backend, las bases de datos y la renderización de páginas dinámicas de forma mucho más robusta y segura que en la versión estática anterior.

### Características Clave de la Migración:
*   **Backend en Django:** Migración completa de una estructura HTML estática a una aplicación dinámica en Django.
*   **Base de Datos Relacional (SQLite):** Configuración de modelos para almacenar los datos de postulaciones y sedes/campus de manera estructurada.
*   **Formularios Dinámicos:** Formulario de postulación que registra los datos directamente en la base de datos a través de modelos Django.
*   **Vistas Modulares:** Separación de la lógica de negocio y presentación usando vistas y templates de Django.
*   **Integración de APIs y Scripts:** Inclusión de secciones dinámicas como la integración de pokemones y uso de almacenamiento local (LocalStorage).

---

## 🛠️ Tecnologías Utilizadas

*   **Framework Principal:** [Django](https://www.djangoproject.com/) (Python)
*   **Base de Datos:** SQLite 3
*   **Frontend:** HTML5, CSS3, JavaScript
*   **Entorno de desarrollo:** Python 3.x

---

## 📂 Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

*   **`portal_talentos/`**: Directorio de configuración global del proyecto Django (configuración de base de datos, urls principales, `settings.py`, `wsgi.py`, etc.).
*   **`alumnos/`**: Aplicación de Django encargada de la lógica de estudiantes y postulaciones.
    *   `models.py`: Definición de los modelos `Campus` y `Postulacion` para la base de datos.
    *   `views.py`: Controladores que renderizan los templates y procesan las peticiones.
    *   `urls.py`: Enrutamiento interno de la aplicación.
    *   `templates/`: Plantillas HTML organizadas por secciones (Talentos, Música, Deportes, Formulario, etc.).
    *   `static/`: Archivos estáticos como hojas de estilo CSS, scripts de JS e imágenes.
*   **`manage.py`**: Utilidad de línea de comandos para la gestión de Django.

---

## 🚀 Instrucciones de Instalación y Ejecución

Sigue estos pasos para levantar el proyecto de manera local en tu entorno de desarrollo:

### 1. Prerrequisitos
Asegúrate de tener instalado Python en tu equipo:
*   [Descargar Python](https://www.python.org/downloads/)

### 2. Clonar o Descargar el Proyecto
Navega a la carpeta del proyecto en tu terminal.

### 3. Crear y Activar un Entorno Virtual (Opcional pero recomendado)
En Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```

### 4. Instalar Django
Instala Django utilizando pip:
```bash
pip install django
```

### 5. Aplicar Migraciones
Prepara la base de datos SQLite y genera las tablas correspondientes a los modelos:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Crear un Superusuario (Opcional)
Para acceder al panel de administración de Django y ver/gestionar las postulaciones registradas:
```bash
python manage.py createsuperuser
```
*(Sigue las instrucciones de la terminal para ingresar usuario, correo y contraseña).*

### 7. Ejecutar el Servidor de Desarrollo
Inicia el servidor local:
```bash
python manage.py runserver
```

Una vez iniciado el servidor, abre tu navegador y entra a:
*   Página Principal: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
*   Administración de Django: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 🏫 Información del Curso
*   **Asignatura:** Programación Web
*   **Docente:** Francisco Javier Calfun
*   **Institución:** Ingeniería en Informática
