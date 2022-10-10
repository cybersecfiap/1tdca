#CRUD - Operações básicas em um banco de dados.

# insert_one & insert_many()
# Funções do insert - definir schema (criar coleções, inserir documentos (create table)

from pymongo import MongoClient
client = MongoClient("localhost", 27017)

#Criar a Base de Dados
#Até aqui não cria a base de dados ele só cria quando inserirmos os dados


db = client.Novo
#db = client["Estudo_mongoDB"]

# Inserindo dados

"""db.pessoas.insert_one({
    "id":10,
    "Nome":"Juquinha",
    "Idade": 45
})"""


"""db.pessoas.insert_one({
    "id":10,
    "Nome":"Juquinha",
    "Idade": 45,
    "filhos": ["Joao", "Pedro", "Marcos"]
})"""

db.pessoas.insert_many(
    [
        {
            "id": 11,
            "nome": "hugo"
        },
        {
            "id": 7,
            "apelido": "jão"
        }
    ]
)




