from flask import Flask, render_template, request
from model import BBDD

app = Flask(__name__)

app.config['STATIC_FOLDER'] = 'static'


@app.route('/')
def menu_principal():
    return render_template('index.html')


@app.route('/materias')
def menu_materias():
    return render_template('menu_materias.html', materias=BBDD.selectAll("Materia"))


@app.route('/materias/crear', methods=['GET'])
def menu_crear_materias():
    return render_template('crear_materia.html')


@app.route('/materias/crear', methods=['POST'])
def crear_materias():
    datos = {}
    # if request.method == 'POST':
    for key in request.form:
        datos[key] = request.form[key]

    datos = BBDD.calcularClave("materia", datos)
    BBDD.insert("materia", datos)
    # return render_template('crear_materia.html')


@app.route('/materias/mostrar', methods=['GET'])
def menu_mostrar_materias():
    datos = BBDD.selectAll("materia")
    print(datos)
    return render_template('mostrar_materias.html', datos=datos)


def lanzar():
    app.run(debug=True)
