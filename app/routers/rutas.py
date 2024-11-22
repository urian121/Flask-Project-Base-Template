from app.controllers import inicio, acerca_de_mi, portafolio, contacto


def registrar_rutas(app):
    @app.route('/')
    def ruta_inicio():
        return inicio()

    @app.route('/acerca-de-mi')
    def ruta_acerca_de_mi():
        return acerca_de_mi()

    # Ruta con parametro opcional
    @app.route('/mi-portafolio/', methods=['GET'])
    @app.route('/mi-portafolio/<nombre>', methods=['GET'])
    def ruta_portafolio(nombre=None):
        return portafolio(nombre)

    @app.route('/contactame')
    def ruta_contacto():
        return contacto()