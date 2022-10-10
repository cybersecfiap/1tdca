#!/usr/bin/env python3

import pymongo
from pymongo import MongoClient

client = pymongo.MongoClient("localhost", 27017)

db = client.graduacao
#collection = db.create_collection("cursos")
collection = db.get_collection('cursos')

'''collection.update_one(
    {'nome_do_curso':'DevOps Engineer'},
    {'$set': {'valor_do_curso':'R$ 2.500,00'}}
)'''

collection.delete_many({ 'valor_do_curso': { '$eq' : 'R$ 2.000,00'}})


'''dados = {
    'nome_do_curso':'DevOps Engineer',
    'vome_do_curso':'R$ 1.800,00',
    'tempo_do_curso':'2 anos',
    'materias_do_Curso':'CLOUD STACK, PRIVATE CLOUD, OPEN SHIFT, TERRAFORM'
}'''


'''dado1 = {
            'nome_do_curso':'Redes de Computadores',
            'valor_do_curso':'R$ 1.900,00',
            'tempo_do_curso':'2 anos',
            'materias_do_curso':'REDES, PROTOCOLO, TELECOM'
}
dado2 = {
            'nome_do_curso': 'Analise de Sistemas',
            'valor_do_curso': 'R$ 2.000,00',
            'tempo_do_curso': '2 anos',
            'materias_do_curso': 'ALGORITMO, CALCULO 1, ESTRUTURA DE DADOS'

}
dado3 = {
            'nome_do_curso': 'Desenvolvimento de Jogos',
            'valor_do_curso': 'R$ 2.100,00',
            'tempo_do_curso': '2 anos',
            'materias_do_curso': 'UX, DESIGN THING, PROGRAMAÇÃO'
}

collection.insert_many([dado1,dado2,dado3])
'''