from conectar import *
import json

db = conexion()
coleccion = db.pedidos

id_pedido = input("Ingrese el id del pedido: ")
id_cliente = int(input("Ingrese el id del cliente: "))
id_libro = input("Ingrese el id del libro: ")
cantidad = float(input("Ingrese la cantidad de libros: "))
precio_total = float(input("Ingrese el precio total del pedido: "))

nuevo_documento = {
    "pedidos": {
        "id_pedido": id_pedido,
        "id_cliente": id_cliente,
        "id_libro": id_libro,
        "cantidad": cantidad,
        "precio_total": precio_total
    }
}

datoInsertado = coleccion.insert_one(nuevo_documento)

print("El pedido ha sido insertado en la base de datos")
