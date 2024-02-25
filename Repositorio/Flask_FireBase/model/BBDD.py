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


def selectOne(tabla, datos):
    try:
        ref = db.reference(tabla)
        return ref.child(datos["clave"]).get()
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


def selectFiltro(tabla, campo, valor):
    return 0
