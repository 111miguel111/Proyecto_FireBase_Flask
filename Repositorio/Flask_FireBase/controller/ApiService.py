from flask import Flask, render_template, request, url_for, redirect
from model import BBDD

app = Flask(__name__)

app.config['STATIC_FOLDER'] = 'static'
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def menu_principal():
    return render_template('index.html')


@app.route('/materias')
def menu_materias():
    return render_template('menu_materias.html', materias=BBDD.selectAll("Materia"))


@app.route('/materias/crear', methods=['GET'])
def menu_crear_materias():
    datos = emptyMateria()
    return render_template('crear_materia.html', datos=datos)


@app.route('/materias/crear', methods=['POST'])
def crear_materias():
    datos = {}
    # if request.method == 'POST':
    for key in request.form:
        datos[key] = request.form[key]

    datos = BBDD.calcularClave("materia", datos)
    BBDD.insert("materia", datos)
    return redirect(url_for('menu_mostrar_materias'))


@app.route('/materias/modificar', methods=['GET'])
def menu_modificar_materias():
    clave = request.args.get('clave')
    datos = BBDD.selectOne("materia", clave)
    if (datos == None):
        datos = emptyMateria()
    return render_template('crear_materia.html', datos=datos)


@app.route('/materias/modificar', methods=['POST'])
def modificar_materias():
    datos = {}
    print("Jaja si")
    # if request.method == 'POST':
    for key in request.form:
        datos[key] = request.form[key]
    print(datos)
    if datos["nombre"] != datos["clave"].split("_")[0]:
        datos = BBDD.calcularClave("materia", datos)
    BBDD.update("materia", datos)
    return redirect(url_for('menu_mostrar_materias'))


@app.route('/materias/mostrar', methods=['GET'])
def menu_mostrar_materias():
    datos = BBDD.selectAll("materia")
    return render_template('mostrar_materias.html', datos=datos)


@app.route('/materias/eliminar', methods=['POST'])
def eliminar_materia():
    datos = request.json
    if (datos != None):
        clave = datos.get("clave")
        materia = BBDD.selectOne("materia", clave)
        if (materia != None):
            BBDD.delete("materia", clave)

    return redirect(url_for('menu_mostrar_materias'))


def emptyMateria():
    datos = {"clave": "", "nombre": "", "descripcion": "", "tipo": "", "nivel": "", "experiencia": "", "fuerza": "",
             "magia": "", "maxpg": "", "maxpm": "", "coste": ""}
    return datos


def lanzar():
    app.run(debug=True)
