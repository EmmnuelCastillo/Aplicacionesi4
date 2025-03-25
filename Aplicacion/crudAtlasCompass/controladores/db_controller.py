from pymongo import MongoClient
import certifi
MONGO_URI = "mongodb+srv://mmnuel5:3qpXk3FrHuA17xLb@cluster0.k7alvsy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["CRUD"]
        return db
    except Exception as e:
        print(f"Error de conexión con la base de datos: {e}")
        return None
