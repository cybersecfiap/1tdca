#!/usr/bin/env python
import pprint
import requests
import ssl

link='https://servicodados.ibge.gov.br/api/v3/agregados/510/periodos/1995/variaveis/216?localidades=N1[all]'


requisicao = requests.get("https://servicodados.ibge.gov.br/api/v3/agregados/510/periodos/1995/variaveis/216?localidades=N1[all]")
informacoes = requisicao.json()
pprint.pprint(informacoes)

