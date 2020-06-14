from pymongo import MongoClient

MONGO_URI = 'mongodb://localhost'
client = MongoClient(MONGO_URI)

db = client['company_register']
collection1 = db['company']
collection2 = db['client']


""" collection1.insert_one({"_id": 1, "nombre": "Daniel", "apellido": "Zamarripa", "direccion": "Av. Bravo 4500 Nueva California"})
collection2.insert_one({"_id": 1, "nombre": "Age Of Empires 2 Definitive Edition", "precio": 200}) """


