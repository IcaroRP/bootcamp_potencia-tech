nome = 'Fulano'
idade = 26
profissao = 'Programador'
linguagem = 'Python'

print('Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.\n' .format(nome, idade, profissao, linguagem))

print('Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}.\n' .format(linguagem, profissao, idade, nome))

print('Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.' .format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))
