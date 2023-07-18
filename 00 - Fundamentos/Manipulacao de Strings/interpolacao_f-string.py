nome = 'Fulano'
idade = 26
profissao = 'Programador'
linguagem = 'Python'

PI = 3.14159

dados = {'nome': 'Fulano', 'idade': 28}

print(f'Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.')

print(f'Valor de PI: {PI:.2f}')

print(f'valor de PI: {PI:10.2f}')


print('Nome: {nome} Idade: {idade}'.format(**dados))