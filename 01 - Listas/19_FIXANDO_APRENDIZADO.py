# Listas
    # Armazenas mais de uma informação em variáveis
    # Manter a sequencia dos dados em uma variável

#               -3             -2            -1
cidades =['Rio de Janeiro', 'São Paulo', 'Salvador'] # Uma lista chamada "cidades"
           # index 0        # index 1     #index 2

#                     -3          -2             -1
produtos_limpeza = ['Sabão', 'Detergente', 'Desinfetante'] # Uma lista de produtos de limpeza
#                      0           1              2

numeros = [2, 4, 6]

#Manipulando listas
print(cidades[-1])

cidades[0] = 'Brasilia' #Troca o dado do item 0 "Rio de Janeiro" por "Brasilia"

#Funções da lista
cidades.append('Santa Catarina') # .append adiciona um item no final da lista
cidades.remove('Salvador') # função auto explicativa
cidades.insert(1, 'Santa Catarina') # inserindo no index 1 Santa catarina no lugar de são paulo
cidades.pop(0) #Retirar um item

# https://docs.python.org/3/tutorial/datastructures.html Lista com todas as funções



#Concatenando listas
letras = ['a', 'b', 'c', 'd']

final = numeros * 4 # para concatenar a mesma litra, nesse caso, 4 vezes

final2 = numeros + letras
#ou
numeros.extend(letras)

print(final2)

#                0                  1
itens = [['item1', 'item2'], ['item3', 'item4']] #uma lista com sub-listas
#            0        1          0        1

print(itens[0][1]) # item2
print(itens[1][1]) # item4