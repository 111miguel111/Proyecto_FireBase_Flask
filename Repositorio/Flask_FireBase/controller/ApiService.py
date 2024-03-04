from flask import Flask, render_template, request, url_for, redirect, jsonify
from model import BBDD  # Importación del modelo de la base de datos

app = Flask(__name__)  # Creación de la instancia de la aplicación Flask

app.config['STATIC_FOLDER'] = 'static'
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def menu_principal():
    """Ruta para el menú principal.

    Returns:
        HTML: Template 'index.html'.
    """
    return render_template('index.html')


# Materias ----------------------------------------------------------------------
# Rutas relacionadas con la gestión de materias

@app.route('/materias')
def menu_materias():
    """Ruta para el menú de materias.

    Returns:
        HTML: Template 'menu_materias.html' con las materias obtenidas de la base de datos.
    """
    return render_template('menu_materias.html', materias=BBDD.selectAll("materia"))


@app.route('/materias/crear', methods=['GET'])
def menu_crear_materias():
    """Ruta para crear una nueva materia.

    Returns:
        HTML: Template 'crear_materia.html' con datos vacíos para una nueva materia.
    """
    datos = emptyMateria()
    return render_template('crear_materia.html', datos=datos)


@app.route('/materias/crear', methods=['POST'])
def crear_materias():
    """Ruta para procesar la creación de una nueva materia.

    Returns:
        Redirect: Redirige al menú de mostrar materias.
    """
    datos = {}
    for key in request.form:
        datos[key] = request.form[key]

    datos = BBDD.calcularClave("materia", datos)
    BBDD.insert("materia", datos)
    return redirect(url_for('menu_mostrar_materias'))


@app.route('/materias/modificar', methods=['GET'])
def menu_modificar_materias():
    """Ruta para modificar una materia existente.

    Returns:
        HTML: Template 'crear_materia.html' con datos de la materia a modificar.
    """
    clave = request.args.get('clave')
    datos = BBDD.selectOne("materia", clave)
    if (datos == None):
        datos = emptyMateria()
    return render_template('crear_materia.html', datos=datos)


@app.route('/materias/modificar', methods=['POST'])
def modificar_materias():
    """Ruta para procesar la modificación de una materia.

    Returns:
        Redirect: Redirige al menú de mostrar materias.
    """
    datos = {}
    for key in request.form:
        datos[key] = request.form[key]
    if datos["nombre"] != datos["clave"].split("_")[0]:
        datos = BBDD.calcularClave("materia", datos)
    BBDD.update("materia", datos)
    return redirect(url_for('menu_mostrar_materias'))


@app.route('/materias/mostrar', methods=['GET'])
def menu_mostrar_materias():
    """Ruta para mostrar todas las materias.

    Returns:
        HTML: Template 'mostrar_materias.html' con todas las materias obtenidas de la base de datos.
    """
    datos = BBDD.selectAll("materia")
    return render_template('mostrar_materias.html', datos=datos)


@app.route('/materias/eliminar', methods=['POST'])
def eliminar_materia():
    """Ruta para eliminar una materia.

    Returns:
        Redirect: Redirige al menú de mostrar materias.
    """
    datos = request.json
    if (datos != None):
        clave = datos.get("clave")
        materia = BBDD.selectOne("materia", clave)
        if (materia != None):
            BBDD.delete("materia", clave)
    return redirect(url_for('menu_mostrar_materias'))


# Armas ----------------------------------------------
# Rutas relacionadas con la gestión de armas

@app.route('/armas')
def menu_armas():
    """Ruta para el menú de armas.

    Returns:
        HTML: Template 'menu_armas.html' con las armas obtenidas de la base de datos.
    """
    return render_template('menu_armas.html', armas=BBDD.selectAll("armas"))


@app.route('/armas/crear', methods=['GET'])
def menu_crear_armas():
    """Ruta para crear una nueva arma.

    Returns:
        HTML: Template 'crear_arma.html' con datos vacíos para una nueva arma.
    """
    datos = emptyMateria()
    return render_template('crear_arma.html', datos=datos)


@app.route('/armas/crear', methods=['POST'])
def crear_armas():
    """Ruta para procesar la creación de una nueva arma.

    Returns:
        Redirect: Redirige al menú de mostrar armas.
    """
    datos = {}
    for key in request.form:
        datos[key] = request.form[key]

    datos = BBDD.calcularClave("armas", datos)
    BBDD.insert("armas", datos)
    return redirect(url_for('menu_mostrar_armas'))


@app.route('/armas/mostrar', methods=['GET'])
def menu_mostrar_armas():
    """Ruta para mostrar todas las armas.

    Returns:
        HTML: Template 'mostrar_armas.html' con todas las armas obtenidas de la base de datos.
    """
    datos = BBDD.selectAll("armas")
    return render_template('mostrar_armas.html', datos=datos)


@app.route('/armas/eliminar', methods=['POST'])
def eliminar_armas():
    """Ruta para eliminar un arma.

    Returns:
        Redirect: Redirige al menú de mostrar armas.
    """
    datos = request.json
    if (datos != None):
        clave = datos.get("clave")
        materia = BBDD.selectOne("armas", clave)
        if (materia != None):
            BBDD.delete("armas", clave)
    return redirect(url_for('menu_mostrar_armas'))


@app.route('/armas/modificar', methods=['GET'])
def menu_modificar_armas():
    """Ruta para modificar un arma existente.

    Returns:
        HTML: Template 'crear_arma.html' con datos del arma a modificar.
    """
    clave = request.args.get('clave')
    datos = BBDD.selectOne("armas", clave)
    if (datos == None):
        datos = emptyMateria()
    return render_template('crear_arma.html', datos=datos)


@app.route('/armas/modificar', methods=['POST'])
def modificar_armas():
    """Ruta para procesar la modificación de un arma.

    Returns:
        Redirect: Redirige al menú de mostrar armas.
    """
    datos = {}
    for key in request.form:
        datos[key] = request.form[key]
    if datos["nombre"] != datos["clave"].split("_")[0]:
        datos = BBDD.calcularClave("armas", datos)
    BBDD.update("armas", datos)
    return redirect(url_for('menu_mostrar_armas'))


def emptyMateria():
    """Crea un diccionario con campos vacíos para una nueva materia.

    Returns:
        dict: Datos vacíos para una nueva materia.
    """
    datos = {"clave": "", "nombre": "", "descripcion": "", "tipo": "", "nivel": "", "experiencia": "", "fuerza": "",
             "magia": "", "maxpg": "", "maxpm": "", "coste": ""}
    return datos


def emptyArma():
    """Crea un diccionario con campos vacíos para una nueva arma.

    Returns:
        dict: Datos vacíos para una nueva arma.
    """
    datos = {"clave": "", "nombre": "", "descripcion": "", "ataque": "", "ataque%": "", "magia": "", "coste": "",
             "materia": "",
             "slot1": "", "slot2": "", "slot3": "", "slot4": "", "slot5": ""
             }
    return datos


def lanzar():
    """Inicia la aplicación Flask en modo debug."""
    app.run(debug=True)


# Personajes ----------------------------------------------
# Rutas relacionadas con la gestión de personajes

@app.route('/personajes')
def menu_personajes():
    """Ruta para el menú de personajes.

    Returns:
        HTML: Template 'menu_personajes.html' con los personajes obtenidos de la base de datos.
    """
    return render_template('menu_personajes.html', personajes=BBDD.selectAll("personajes"))


@app.route('/personajes/crear', methods=['GET'])
def menu_crear_personajes():
    """Ruta para crear un nuevo personaje.

    Returns:
        HTML: Template 'crear_personaje.html' con datos vacíos para un nuevo personaje.
    """
    datos = emptyMateria()
    return render_template('crear_personaje.html', datos=datos)


@app.route('/personajes/crear', methods=['POST'])
def crear_personajes():
    """Ruta para procesar la creación de un nuevo personaje.

    Returns:
        Redirect: Redirige al menú de mostrar personajes.
    """
    datos = {}
    for key in request.form:
        datos[key] = request.form[key]

    datos = BBDD.calcularClave("personajes", datos)
    BBDD.insert("personajes", datos)
    return redirect(url_for('menu_mostrar_personajes'))


@app.route('/personajes/mostrar', methods=['GET'])
def menu_mostrar_personajes():
    """Ruta para mostrar todos los personajes.

    Returns:
        HTML: Template 'mostrar_personajes.html' con todos los personajes obtenidos de la base de datos.
    """
    datos = BBDD.selectAll("personajes")
    return render_template('mostrar_personajes.html', datos=datos)


@app.route('/personajes/eliminar', methods=['POST'])
def eliminar_personajes():
    """Ruta para eliminar un personaje.

    Returns:
        Redirect: Redirige al menú de mostrar personajes.
    """
    datos = request.json
    if (datos != None):
        clave = datos.get("nombre")
        materia = BBDD.selectOne("personajes", clave)
        if (materia != None):
            BBDD.delete("personajes", clave)
    return redirect(url_for('menu_mostrar_personajes'))


@app.route('/personajes/modificar', methods=['GET'])
def menu_modificar_personajes():
    """Ruta para modificar un personaje existente.

    Returns:
        HTML: Template 'crear_personaje.html' con datos del personaje a modificar.
    """
    clave = request.args.get('nombre')
    datos = BBDD.selectOne("personajes", clave)
    if (datos == None):
        datos = emptyMateria()
    return render_template('crear_personaje.html', datos=datos)


@app.route('/personajes/modificar', methods=['POST'])
def modificar_personajes():
    """Ruta para procesar la modificación de un personaje.

    Returns:
        Redirect: Redirige al menú de mostrar personajes.
    """
    datos = {}
    for key in request.form:
        datos[key] = request.form[key]
    if datos["nombre"] != datos["nombre"]:
        datos = BBDD.calcularClave("personajes", datos)
    BBDD.update("personajes", datos)
    return redirect(url_for('menu_mostrar_personajes'))


# Llenar bbdd --------------------------------------------------
# Rutas relacionadas con el llenado de la base de datos

@app.route('/bbdd')
def menu_bbdd():
    """Ruta para el menú de la base de datos.

    Returns:
        HTML: Template 'menu_bbdd.html'.
    """
    return render_template('menu_bbdd.html')


@app.route('/bbdd/llenar')
def meter_datos():
    """Ruta para llenar la base de datos con datos de ejemplo.

    Returns:
        Redirect: Redirige al menú de la base de datos.
    """
    i = 1
    cont = 1
    while i <= 10:
        tipoMateria = ""
        match cont:
            case 1:
                tipoMateria = "magia"
            case 2:
                tipoMateria = "invocacion"
            case 3:
                tipoMateria = "soporte"
            case 4:
                tipoMateria = "comando"
            case 5:
                tipoMateria = "independiente"
                cont = 0
        cont += 1


        BBDD.insert("materia",
                    {"clave": "sampleM_" + str(i),
                     "nombre": "Sample Materia" + str(i),
                     "descripcion": "Ejemplo",
                     "tipo": tipoMateria,
                     "nivel": str(cont),
                     "experiencia": str(i),
                     "fuerza": str(i),
                     "magia": str(i),
                     "maxpg": str(i),
                     "maxpm": str(i),
                     "coste": str(i)})

        BBDD.insert("armas",
                    {"clave": "sampleW_" + str(i),
                     "nombre": "Sample Arma" + str(i),
                     "descripcion": "Ejemplo",
                     "ataque": str(i),
                     "ataquePor": str(i),
                     "magia": str(i),
                     "coste": str(i),
                     "materia": str(cont),
                     "slot1": "sample_m_" + str(i),
                     "slot2": "sample_m_" + str(i),
                     "slot3": "sample_m_" + str(i)})
        i += 1
    return redirect(url_for('menu_bbdd'))


@app.route('/bbdd/borrar')
def borrar_datos():
    """Ruta para borrar todos los datos de la base de datos.

    Returns:
        Redirect: Redirige al menú de la base de datos.
    """
    BBDD.dropDDBB()
    return redirect(url_for('menu_bbdd'))


@app.route("/bbdd/materia", methods=['GET'])
def get_all():
    datos = BBDD.selectAll("materia")
    return jsonify(datos)
