#!/usr/bin/env python3

from sklearn import tree

casapequena=0
casamedia=1
casagrande=2

valor = [[70], [120], [140], [160]]
#tamanho =[[casapequena], [casamedia], [casagrande]]
tamanho =[[70000], [12000], [140000], [160000]]

classificador = tree.DecisionTreeClassifier()
classificador = classificador.fit(valor, tamanho)

metros = input("Por favor, entre com a metragem da casa: ")
# categoria = input("Por favor, informe a superficie, (0) pequena, (1) media, (2) grande : ")

resultodousuario = classificador.predict([[metros]])
print(resultodousuario)
