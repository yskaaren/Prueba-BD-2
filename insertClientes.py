from conectar import *
import json

db = conexion()
coleccion = db.clientes

id_cliente = input("Ingrese el id del cliente: ")
nombre = input("Ingrese el nombre del cliente: ")
email = input("Ingrese el email del cliente: ")

nuevo_documento = {
    "clientes": {
        "id_cliente": id_cliente,
        "nombre": nombre,
        "email": email
    }
}

datoInsertado = coleccion.insert_one(nuevo_documento)

print("El cliente ha sido insertado en la base de datos")
