from flask import Flask, render_template, request, redirect, url_for
# from reactpy import component, html


active = 'index'

app = Flask(__name__)  # Instancia de Flask

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
