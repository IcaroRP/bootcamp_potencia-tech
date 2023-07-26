'''
Conjuntos em python não suportam indexação e nem fatiamento,
caso queria acessar os seus valores é necessário convverter
o conjunto para lista

'''

numeros = {1, 2, 3, 2}

numeros = list(numeros)

numeros[0]