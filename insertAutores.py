from conectar import *
import json

db = conexion()
coleccion = db.autores

autor_id = input("Ingrese el id del autor: ")
nombre_autor = input("Ingrese el nombre del autor: ")
nacionalidad = input("Ingrese la nacionalidad: ")

nuevo_documento = {
    "autores": {
        "autor_id": autor_id,
        "nombre_autor": nombre_autor,
        "nacionalidad": nacionalidad,
    }
}

datoInsertado = coleccion.insert_one(nuevo_documento)

print("El autor ha sido insertado en la base de datos")
