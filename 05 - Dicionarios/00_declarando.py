'''
Um dicionario é um conjunto não-ordenado de pares
chave:valor, onde as chaves são unicas em uma dada instância
do dicionario; Dicionários são delimitados por chaves: {},
e contém uma lista de pares chave: valor separada por virgulas

'''

pessoa = {"nome": "Guillerme", "idade": 28}
#          chave      valor     chave   valor

pessoa["telefone"] = "3333-1234" # {"nome": "Guillerme", "idade": 28, "telefone": "3333-1234"}

pessoa_alt = dict(nome="Guillherme", idade=28)
#                         chave       valor
