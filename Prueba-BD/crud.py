from conectar import *
import json
from bson.objectid import ObjectId

db = conexion()
coleccion_libros = db.libros
coleccion_autores = db.autores
coleccion_clientes = db.clientes
coleccion_pedidos = db.pedidos

def insertar_libro(libro):
    try:
        coleccion_libros.insert_one(libro)
        return True
    except Exception as error:
        print("Error al insertar libro", error)     
        return False   
    
def modificar_libro(id_libro, libro):
        if coleccion_libros.find_one(id_libro):
            return False
        else:
            coleccion_libros.update_one(libro)
            print("El libro fue modificado exitosamente")
    

def eliminar_libro(id_libro):
    try:
        coleccion_libros.delete_one({'_id': ObjectId(id_libro)})
        return True
    except Exception as error:
        print("Error al eliminar libro", error)     

def insertar_autor(autores):
    try:
        coleccion_autores.insert_one(autores)
        return True
    except Exception as error:
        print("Error al insertar autor", error)     
        return False   

def eliminar_autor(id_autor):
    try:
        coleccion_autores.delete_one({'_id': ObjectId(id_autor)})
        return True
    except Exception as error:
        print("Error al eliminar autor", error)     
        

def insertar_cliente(cliente):
    try:
        coleccion_clientes.insert_one(cliente)
        return True
    except Exception as error:
        print("Error al insertar cliente", error)     
        return False   
    
def eliminar_cliente(id_cliente):
    try:
        coleccion_clientes.delete_one({'_id': ObjectId(id_cliente)})
        return True
    except Exception as error:
        print("Error al eliminar cliente", error) 

def insertar_pedido(pedido):
    try:
        coleccion_pedidos.insert_one(pedido)
        return True
    except Exception as error:
        print("Error al insertar pedido", error)     
        return False   
    
def eliminar_pedido(id_pedido):
    try:
        coleccion_pedidos.delete_one({'_id': ObjectId(id_pedido)})
        return True
    except Exception as error:
        print("Error al eliminar pedido", error) 