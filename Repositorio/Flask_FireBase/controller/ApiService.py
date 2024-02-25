from flask import Flask, render_template, request
from model import BBDD

app = Flask(__name__)

app.config['STATIC_FOLDER'] = 'static'


@app.route('/menu')
def menu_principal():
    return render_template('index.html')


@app.route('/materias')
def menu_materias():
    return render_template('menu_materias.html', materias=BBDD.selectAll("Materia"))


@app.route('/materias/crear', methods=['GET', 'POST'])
def crear_materias():
    datos = {}
    # if request.method == 'POST':
    for key in request.form:
        datos[key] = request.form[key]

    print(datos)


def lanzar():
    app.run(debug=True)
