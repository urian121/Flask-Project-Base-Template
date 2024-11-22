from flask import render_template, jsonify

def inicio():
    return render_template('index.html')

def acerca_de_mi():
    return render_template('pages/acerca.html')

def portafolio(nombre):
    return render_template('pages/portafolio.html', nombre=nombre)

def contacto():
    return render_template('pages/contacto.html')
