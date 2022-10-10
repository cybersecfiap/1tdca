#!/usr/bin/env python3.9
import pymongo
#from pymongo import MongoClient

#cluster = pymongo.MongoClient("mongodb+srv://fiapuser:<password>@fiapcluster.r53si5q.mongodb.net/test")


#Conectando ao Banco de Dados
client = pymongo.MongoClient("mongodb+srv://fiapuser:Fiap#@123@fiapcluster.wy0d2sp.mongodb.net/?retryWrites=true&w=majority")

#Enviando a informação que queremos criar a Base Fiap
db = client.faculdade_fiap

#Enviando a informação que queremos criar uma collection chamada aluno
#collection = db.create_collection("alunos")

#Inserindo Dados

#insert_one

#db.client.Fiap.alunos.delete_many({'nome_aluno': { '$eq' : 'Marcos Cortez   ' }})


#for dados in resultado:
#   print(dados)

#if resultado:
#    print(resultado)
#else:
#    print("Valor não encontrado.")


#for dado in resultado:
#    print(dado['email_aluno'])

#resultado = db.client.Fiap.alunos.find_one({'nome_aluno':'Fqbio Pires'})
#if resultado:
#    print(resultado)
#else:
#    print("Nada foi encontrado")
#db.client.faculdade_fiap.alunos.update_one(
#     {'nome_aluno':'Alberico Japa'},
#     {'$set': {'idade_aluno':'40'}}
#)



db.client.faculdade_fiap.insert_many(
    [
        {
            'nome_aluno':'Marcos Cortez',
            'email_aluno':'cortez@fiap.com.br',
            'vida_aluno':'22'
        },
        {
            'nome_aluno':'Alberico Japa',
            'contato_aluno':'japa@fiap.com.br',
            'idade_aluno':'30'

        },
        {
            'apelido_aluno':'Gustavo Lima',
            'email_aluno':'glima@fiap.com.br',
            'idade_aluno':'35'
        }
    ]
)
