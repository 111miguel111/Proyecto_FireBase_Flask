import firebase_admin
from firebase_admin import credentials, db, firestore
import traceback

cred = credentials.Certificate("proyecto-firebase-flask-fdef4-firebase-adminsdk-pppt6-cc2ea7ffe1.json")

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://proyecto-firebase-flask-fdef4-default-rtdb.europe-west1.firebasedatabase.app/'})


def insert(tabla, datos):
    try:
        ref = db.reference(tabla)
        ref.child(datos["clave"]).set(datos)
        return True
    except:
        print(traceback.format_exc())
    return False


def delete(tabla, clave):
    try:
        ref = db.reference(tabla)
        elemento = ref.child(clave)
        elemento.delete()
        return True
    except:
        print(traceback.format_exc())
    return False


def update(tabla, datos):
    try:
        ref = db.reference(tabla)
        elemento = ref.child(datos["clave"])
        elemento.update(datos)
        return True
    except:
        print(traceback.format_exc())
    return False


def selectOne(tabla, clave):
    try:
        ref = db.reference(tabla)
        return ref.child(clave).get()
    except:
        print(traceback.format_exc())
    return None


def selectAll(tabla):
    try:
        ref = db.reference()
        return ref.child(tabla).get()
    except:
        print(traceback.format_exc())
    return None

def dropDDBB():
    try:
        ref = db.reference()
        ref.set({})
    except:
        print(traceback.format_exc())


def selectFiltro(tabla, campo, valor):
    return 0


def calcularClave(tabla, datos):
    elementos = selectAll(tabla)
    if elementos != None:
        cont = 0
        for elemento in elementos:
            if (elementos[elemento]["nombre"] == datos["nombre"]):
                num = elementos[elemento]["clave"].split('_')[1]
                if (int(num) > cont):
                    cont = int(num)
        datos["clave"] = datos["nombre"] + "_" + str((cont + 1))
    else:
        datos["clave"] = datos["nombre"] + "_" + str(1)
    return datos
