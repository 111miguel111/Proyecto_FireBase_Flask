import firebase_admin
from firebase_admin import credentials, db, firestore
import traceback

# Credenciales de Firebase
cred = credentials.Certificate("proyecto-firebase-flask-fdef4-firebase-adminsdk-pppt6-cc2ea7ffe1.json")

# Inicialización de la aplicación de Firebase
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://proyecto-firebase-flask-fdef4-default-rtdb.europe-west1.firebasedatabase.app/'})


def insert(tabla, datos):
    """
    Inserta datos en la base de datos.

    Args:
        tabla (str): Nombre de la tabla en la base de datos.
        datos (dict): Datos a insertar en forma de diccionario.

    Returns:
        bool: True si la operación es exitosa, False si no lo es.
    """
    try:
        ref = db.reference(tabla)
        ref.child(datos["clave"]).set(datos)
        return True
    except:
        print(traceback.format_exc())
    return False


def delete(tabla, clave):
    """
    Elimina un elemento de la base de datos.

    Args:
        tabla (str): Nombre de la tabla en la base de datos.
        clave (str): Clave del elemento a eliminar.

    Returns:
        bool: True si la operación es exitosa, False si no lo es.
    """
    try:
        ref = db.reference(tabla)
        elemento = ref.child(clave)
        elemento.delete()
        return True
    except:
        print(traceback.format_exc())
    return False


def update(tabla, datos):
    """
    Actualiza un elemento existente en la base de datos.

    Args:
        tabla (str): Nombre de la tabla en la base de datos.
        datos (dict): Datos actualizados en forma de diccionario.

    Returns:
        bool: True si la operación es exitosa, False si no lo es.
    """
    try:
        ref = db.reference(tabla)
        elemento = ref.child(datos["clave"])
        elemento.update(datos)
        return True
    except:
        print(traceback.format_exc())
    return False


def selectOne(tabla, clave):
    """
    Recupera un único elemento de la base de datos.

    Args:
        tabla (str): Nombre de la tabla en la base de datos.
        clave (str): Clave del elemento a recuperar.

    Returns:
        dict: Elemento recuperado si la operación es exitosa, None si no lo es.
    """
    try:
        ref = db.reference(tabla)
        return ref.child(clave).get()
    except:
        print(traceback.format_exc())
    return None


def selectAll(tabla):
    """
    Recupera todos los elementos de una tabla específica de la base de datos.

    Args:
        tabla (str): Nombre de la tabla en la base de datos.

    Returns:
        dict: Todos los elementos recuperados si la operación es exitosa, None si no lo es.
    """
    try:
        ref = db.reference()
        return ref.child(tabla).get()
    except:
        print(traceback.format_exc())
    return None


def dropDDBB():
    """
    Elimina toda la base de datos.
    """
    try:
        ref = db.reference()
        ref.set({})
    except:
        print(traceback.format_exc())


def selectFiltro(tabla, campo, valor):
    """
    Realiza una selección filtrada en la base de datos.

    Args:
        tabla (str): Nombre de la tabla en la base de datos.
        campo (str): Campo para filtrar.
        valor (str): Valor a filtrar.

    Returns:
        int: No implementado, siempre devuelve 0.
    """
    return 0


def calcularClave(tabla, datos):
    """
    Calcula la clave para un nuevo elemento que se va a insertar en la base de datos.

    Args:
        tabla (str): Nombre de la tabla en la base de datos.
        datos (dict): Datos del nuevo elemento en forma de diccionario.

    Returns:
        dict: Datos con la clave calculada.
    """
    elementos = selectAll(tabla)
    if elementos != None:
        cont = 0
        for elemento in elementos:
            if elementos[elemento]["nombre"] == datos["nombre"]:
                num = elementos[elemento]["clave"].split('_')[1]
                if (int(num) > cont):
                    cont = int(num)
        datos["clave"] = datos["nombre"] + "_" + str((cont + 1))
    else:
        datos["clave"] = datos["nombre"] + "_" + str(1)
    return datos


def obtenerVariasArmasPorClave(clave):
    """
    Recupera varios elementos de la tabla de armas de la base de datos según una clave dada.

    Args:
        clave (str): Clave para la búsqueda.

    Returns:
        dict: Diccionario de armas que coinciden con la clave proporcionada.
    """
    ref = db.reference("armas")  # Reemplaza "tu-nodo" con la ruta de tu nodo en la base de datos
    ocurrencias = {}

    # Obtener todas las claves que comienzan con el prefijo dado
    if clave != "":
        keys = ref.order_by_key().start_at(clave).end_at(clave + "\uf8ff").get()
        for key, value in keys.items():
            # Añadir cada ocurrencia al diccionario
            ocurrencias[key] = value
    else:
        ocurrencias = ref.get()
    print(ocurrencias)
    return ocurrencias
