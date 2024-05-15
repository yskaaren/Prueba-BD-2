from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Agreguen si string de conexion
url = "mongodb+srv://karengutierrez14:Naritaa14@serverinacap.8ri8bib.mongodb.net/?retryWrites=true&w=majority&appName=ServerInacap"

# sample_restaurants.restaurants


def conexion():
    cliente = MongoClient(url, server_api=ServerApi('1'))
    try:
        cliente.admin.command('ping')
        print("La conexion a la base de datos es correcta.")
        db = cliente.libreria
        return db
    except Exception as e:
        print("ERROR")
        print(e)
