#Importando o PYmongo

#import pymongo

#Importando Pymongo MongoClient

from pymongo import MongoClient

client = MongoClient("localhost", 27017)
print(client.list_database_names())

db = client.Estudo_MongoDB
db.teste.insert_one(
    {
        "bala":"Juquinha"
    }
)

"""db.teste.insert_many(
    [
        {"id": 1},
        {"id": 12},
        {"id": 500},
        {"id": -222}
    ]
)"""