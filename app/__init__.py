from flask import Flask, redirect, url_for # Importando algunas funciones desde Flask
from config import DevelopmentConfig # # Importando la configuración del proyecto
from app.routers import registrar_rutas  # Importando todas las rutas desde Routers


# Definimos la función create_app() que es responsable de crear y devolver la aplicación Flask.
def create_app():
    # # Inicialización de la aplicación Flask
    app = Flask(__name__, static_folder="static", template_folder="templates")

    # Cargar la configuración desde config.py
    app.config.from_object(DevelopmentConfig)

    # Debugging: verifica configuraciones cargadas
    # print(f"Secret Key: {app.config['SECRET_KEY']}")
    # print(f"Debug: {app.config['DEBUG']}")

    # Registrar rutas directamente
    registrar_rutas(app)

    # Manejo de error 404
    @app.errorhandler(404)
    def not_found(error):
        return redirect(url_for('inicio'))

    # Retornar la instancia de la aplicación Flask
    return app
