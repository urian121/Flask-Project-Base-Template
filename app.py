from app import create_app
from config import Config

# Crear la instancia de la app
app = create_app()


if __name__ == "__main__":
    # Ejecutar la app usando configuraciones globales
    app.run(debug=Config.DEBUG, host=Config.HOST, port=Config.PORT)
