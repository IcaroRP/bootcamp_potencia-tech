lista = ['p', 'y', 't', 'h', 'o', 'n']

lista[2:] # ['t', 'h', 'o', 'n']
lista[:2] # ['p', 'y']
lista[1:3] # ['y', 't']
lista[0:3:2] # ['p', 't']
lista[::] # ['p', 'y', 't', 'h', 'o', 'n']
lista[::-1] # ['n', 'o', 'h', 't', 'y', 'p']

# percorrendo todo o conteudo presente na lista
for conteudo in lista:
    print(conteudo)

print()    

'''
NUMERANDO: 
indice == contador
carro == item da iteração
'''    

carros = ['gol', 'celta', 'palio']

for indice, carro in enumerate(carros):
    print(f'{indice}: {carro}')