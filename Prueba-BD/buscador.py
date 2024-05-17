from conectar import *
import json
from bson import json_util

#"restaurant_id": "40356483"
buscar = input("Ingrese id del restaurante: ")

db = conexion() 
coleccion = db.restaurants
documentos = coleccion.find({"restaurant_id": buscar})

resultados = []

for documento in documentos:
    documento['_id'] = str(documento['_id'])
    resultados.append(documento)
    
print(json_util.dumps(resultados, indent = 4))