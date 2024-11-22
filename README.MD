# Flask Project Base Template 🚀


**`flask-project-base-template`** es un punto de partida bien estructurado para proyectos web con Flask. Proporciona una organización clara de carpetas, rutas y archivos de configuración, templa

- Configuración de base de datos.  
- Soporte para pruebas.  
- Una base sólida para comenzar rápidamente y desarrollar aplicaciones web de forma eficiente.
- Manejo de rutas
- Manejo de rutas no encontradas con `status 404`
- Template base e integración con `include` y `url_for`.  
- Manejo de archivos estáticos.  
- Modularidad mediante el uso de `__init__.py`.  
- Estructura más modular y organizada, separando el código en carpetas específicas:  
  - **`routers/`**: Aquí se definen todas las rutas de la aplicación.  
  - **`controllers/`**: Se gestionan las funciones según los módulos existentes (ejemplo: `controllerUser.py`, `controllerHome.py`, etc.).  
  

## Resultado Final

![Resultado Final](https://raw.githubusercontent.com/urian121/imagenes-proyectos-github/refs/heads/master/Flask_Project_Base_Template.gif)

---


#### Estructura del proyecto
```bash
flask-project-base-template/
│
├── app/
│   ├── controllers/
│   ├── routers/
│   ├── static/
│   ├── templates/
│   │   ├── api/
│   │   ├── bases/
│   │   ├── pages/
│   │   └── index.html
│   ├── __init__.py
│   ├── app.py
│   ├── requirements.txt
│   └── config.py
│
├── tests/
│   ├── test_basic.py
│   └── test_routes.py
│
├── .gitignore
├── README.md
└── vercel.json
```

### Notas

El archivo `__init__.py` dentro de la carpeta `app/` tiene la función de inicializar y configurar la aplicación Flask, preparando todo lo necesario para que la aplicación se ejecute correctamente. Además sirve como el punto de entrada para crear y configurar la instancia de la aplicación.

La función `create_app()` es el punto de entrada para la creación de la aplicación, además retorna la instancia de la aplicación Flask, que es la que se usará para ejecutar el servidor o desplegar la app.

1. Se inicializa la aplicación Flask con configuraciones como el directorio de archivos estáticos y templates.
2. Se carga la configuración desde el archivo `config.py` (en este caso, `DevelopmentConfig`).
3. Se registran las rutas de la aplicación importando y ejecutando la función `'registrar_rutas'` del archivo `'routers'`.
4. Se configura el manejo de errores `404`, redirigiendo a la ruta de inicio.


- **Archivo `controllers/__init__.py`:**  
  Está configurado para exportar todas las funciones definidas en el archivo `handlers.py`, permitiendo que estén disponibles directamente desde `controllers` al importar.

- **Archivo `routers/__init__.py`:**  
  Está configurado para exportar todas las rutas registradas en el archivo `rutas.py`, facilitando su importación directa desde `routers`.

## Cómo Correr el Proyecto 🚀  

**1. Crear un entorno virtual:**  
   Si no sabes cómo hacerlo, aquí tienes una [guía paso a paso](https://www.urianviera.com/python/crear-entornos-virtuales-en-python).
   No olvides activar tu entorno virtual.
**2. Instalar las dependencias del proyecto:**  
   Ejecuta el siguiente comando para instalar todas las librerías necesarias:  
   ```bash
   pip install -r requirements.txt
   ```
**3. Ejecutar el proyecto**
   ```bash
   python app.py
   ```
**4. Visitar la URL**
   http://localhost:8000


### Expresiones de Gratitud 🎁

- Ayuda a difundir este proyecto compartiéndolo con otros 📢  
- Invítame una cerveza 🍺 o un café ☕ (Paypal: iamdeveloper86@gmail.com)  
- Agradece públicamente 🤓, ¡me alegrará saberlo!  
- Y no olvides dejar tu estrella ⭐ en el repositorio... **¡dicen que trae buena suerte!** 🍀  

## No olvides SUSCRIBIRTE 👍
