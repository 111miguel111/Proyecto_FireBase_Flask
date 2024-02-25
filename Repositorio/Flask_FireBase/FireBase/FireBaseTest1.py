import firebase_admin
from firebase_admin import credentials, db, firestore

'''
*******
Video para configurar la cuenta:
https://www.youtube.com/watch?v=FR1hLBRYj0o
*******


Ejemplos interesantes:
https://morioh.com/p/a593f973aff0
https://firebase.google.com/docs/database/security/indexing-data?authuser=0
https://firebase.googleblog.com/2017/07/accessing-database-from-python-admin-sdk.html

Junto con la libreria json
https://www.freecodecamp.org/news/how-to-get-started-with-firebase-using-python/

Documentacion oficial:
https://firebase.google.com/docs/reference/admin/python

'''

print("Empezamos")

# Cargamos el certificado
cred = credentials.Certificate("proyecpython01-firebase-adminsdk-whyz9-d4f31f98a3.json")

# Hacemos referencia a la base de datos en tiempo real
firebase_admin.initialize_app(cred,
                              {'databaseURL': 'https://proyecpython01-default-rtdb.europe-west1.firebasedatabase.app/'})

# Creamos una coleccion de libros
ref = db.reference('libros')
ref.push({'titulo': 'titulo1', 'editor': 'editor1', 'anyo': 1991})
ref.push({'titulo': 'titulo2', 'editor': 'editor2', 'anyo': 1992})
ref.push({'aa': 'aaa', 'bb': 'bbb', 'cc': "ddd"})
# Push crea una clave aleatoria para cada elemento
# Para un alta y elegir la clave
ref.child("miclave").set({'titulo': 'titulo2', 'editor': 'editor2', 'anyo': 1992})

# Esto es solo para aniadir datos al principio
# El set borra el contenido anterior si existiera. No valdria para ANIADIR
ref = db.reference('libros')
ref.set({'libro001': {
    'titulo': 'red',
    'editor': 1,
    'height': 3,
    'length': 2
},
    'libro002': {
        'titulo': 'green',
        'editor': 1,
        'height': 2,
        'length': 3
    },
    'libro003': {
        'titulo': 'yellow',
        'editor': 3,
        'height': 2,
        'length': 1
    }})

ref = db.reference('revistas')
ref.set({'rev001': {
    'color': 'red',
    'width': 1,
    'height': 3,
    'length': 2
},
    'rev002': {
        'color': 'green',
        'width': 1,
        'height': 2,
        'length': 3
    },
    'rev003': {
        'color': 'yellow',
        'width': 3,
        'height': 2,
        'length': 1
    }})

# Cojo TODA la base de datos
result = db.reference()
print(result, type(result))

# Mostraria los distintos tipos de documentos
print("PAREJAS CLAVE-VALOR: ", result.get().items())
print()
print("CLAVES: ", result.get().keys())
print()
print("VALORES: ", result.get().values())
print()
# print("Num elementos:",len(result.get().values()))
print()
print("LIBROS", result.get()['libros'])
print()
for i in result.get()['libros'].keys():
    print(i)
    print("***", result.get()['libros'][i])

# Muestro cada elemenmto por separado
for i in result.get()['libros'].keys():
    print(i)
    for j in result.get()['libros'][i].keys():
        print("\t ", j, ":", result.get()['libros'][i][j])

# Mostrar todo
root = db.reference()  # Cogemos un objeto que representa a TODA la BD

# Imprimo las claves de otra  forma
for i in root.child('libros').get():
    print(i)

print("***********")
root = db.reference('libros')  # Cogemos un objeto que representa solo la coleccion 'libros'
for i in root.get():  # get para coger TODOS los documentos 'libros'
    print(i)  # Clave de cada documento
    elemento = root.child(i).get()  # cojo un elemento concreto por su clave
    print("elemento completo:", elemento)
    print("campos:", elemento.keys())
    print("Campo titulo:", elemento['titulo'])
    # Iterar sin for
    elementos = iter(elemento.keys())
    firstKey = next(elementos)
    print("Primer campo:", elemento[firstKey])

'''
Reglas para poder hacer busquedas
{
  "rules": {
    ".read": true,
    ".write": true,
    "libros": {
      ".indexOn": ["titulo", "editor", "height", "length"]
    }
  }
}
'''

print("***********")

# Buscar un elemento en la coleccion 'libros'
root = db.reference('libros')
# Query generator para libros; recupera TODOS los libros con titulo 'titulo1'
baseDatos = firestore.client()
results = baseDatos.collection('libros').where('titulo', '==', 'titulo1').stream()
print(results)
'''
#Funciona en FIRESTORE. La otra base de datos
if results.exists:
	print("EXISTE")
print("------")
results = baseDatos.collection('libros').where('titulo', '==', 'red').stream()
for i in results:
	#print(i)
	print(f'{i.id} => {i.to_dict()}')
'''

# Buscar
print("\n*****BUSCAR\n")
resultado = root.order_by_child('titulo').equal_to("titulo2").get()
if (not resultado):
    print("No se ha encontrado nada")
resultado = root.order_by_child('titulo').equal_to("red").get()
for key in resultado:
    print(key)
    elemento = root.child(key).get()
    print("elemento completo:", elemento)

'''
Mas opciones de busqueda en:
https://morioh.com/p/a593f973aff0
'''

print("\n*****MODIFICACION\n")
# Modifica el titulo
resultado = root.order_by_child('titulo').equal_to("titulo1").get()
if resultado:
    field_updates = {"titulo": "titulo111"}
    for key in resultado:
        print(key)
        elemento = root.child(key)
        elemento.update(field_updates)  # Modificamos el campo
        print("elemento completo:", elemento.get())
else:
    print("Documento no encontrado")
    resultado = root.order_by_child('titulo').equal_to("yellow").get()
    print(type(resultado), resultado.keys(), resultado.values())
    for key in resultado:
        elemento = root.child(key)
        elemento.update({'titulo': 'titulo1'})
        print("elemento restaurado:", elemento.get())

print("\n*****BORRADO\n")
resultado = root.order_by_child('titulo').equal_to("green").get()
if resultado:
    print("Si exite el elemento a borrar")

    # Otra forma de acceder a un elemento
    elemento = list(resultado.values())[0]
    print(elemento)

    for key in resultado:
        elemento = root.child(key)
        confirmacion = input("Estas seguro de querer borrar?s/n")
        if (confirmacion.lower() == 's'):
            elemento.delete()

input("Pulsa intro para continuar. Antes revisa los datos de la BD")
resultado = root.order_by_child('titulo').equal_to("titulo1").get()
if not resultado:
    ref = db.reference('libros')
    ref.push({'titulo': 'titulo1', 'editor': 'editor1', 'anyo': 1990})

print("Fin")

# modificamos
# ref = db.reference('libros')
'''
libro_ref = db.child('libros').get()
for i in libro_ref:
    print(i)
'''
