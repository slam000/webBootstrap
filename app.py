from flask import Flask, render_template, request, redirect, url_for
import os
import json


active = 'index'

app = Flask(__name__)  # Instancia de Flask

def compruebajson(ruta_json):
    if not os.path.exists(ruta_json):
        # Crear una lista de experiencias
        experiencias = [
            {
                "fechainicio": "2020-01-01",
                "fechafin": "2022-01-01",
                "titulo": "Ingeniero de Software",
                "experiencia": "Desarrollo de aplicaciones web",
                "claves": ["Python", "Flask", "JavaScript"]
            },
            {
                "fechainicio": "2018-01-01",
                "fechafin": "2020-01-01",
                "titulo": "Desarrollador Full Stack",
                "experiencia": "Desarrollo de aplicaciones full stack",
                "claves": ["Python", "Django", "React"]
            }
        ]
        # Escribir la lista de experiencias al archivo JSON
        with open(ruta_json, 'w') as f:
            json.dump(experiencias, f)

# Pagina de inicio
@app.route('/')
@app.route('/index')
def index():
    active = 'Inicio'
    menu = getMenu()
    return render_template('index.html', menu=menu, active=active)

# Página sobre mi
@app.route('/about')
def about():
    active = 'Acerca de'
    menu = getMenu()
    return render_template('about.html', menu=menu, active=active)

# Página de experiencia
@app.route('/resume')   
def resume():
    active = 'Experiencia'
    menu = getMenu()
    return render_template('resume.html', menu=menu, active=active) 

# Página de contacto
@app.route('/contact')
def contact():
    active = 'Contacto'
    menu = getMenu()
    return render_template('contact.html', menu=menu, active=active)

# Devuelve el menú
def getMenu():
    return [
        {'url': 'index', 'texto': 'Inicio'},
        {'url': 'about', 'texto': 'Acerca de'},
        {'url': 'resume', 'texto': 'Experiencia'},
        {'url': 'contact', 'texto': 'Contacto'},
    ]   

@app.errorhandler(500)  # Manejador de errores
def error500(e):
    return render_template('500.html'), 500 
    

    
if __name__ == '__main__':
    app.run(debug=True, port=5000) # debug=True y puerto es opcional
