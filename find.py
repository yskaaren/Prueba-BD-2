from conectar import *
import json
from bson import json_util
# db.coleccion.
db = conexion() # sample_restaurants
coleccion = db.restaurants
documentos = coleccion.find()
# db.coleccion.find()

resultados = []

for documento in documentos:
    documento['_id'] = str(documento['_id'])
    resultados.append(documento)
    
print(json_util.dumps(resultados, indent = 4))