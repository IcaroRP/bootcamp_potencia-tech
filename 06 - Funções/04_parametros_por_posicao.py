'''
Por padrão, argumentos podem ser passados para uma função
python tanto por posição quanto explicitamento pelo nome.
Para uma melhor legibilidade e desempenho, faz sentido restringir
a meneira pelo qual argumentos possam ser passados, assim um
desenvolvedor precisa apenas olhar para a definição da afunção para
determinar se os itens são passados por posição, por posição e nome
ou por nome.

'''

'''
Tudo até a / é possição e tudo depois de * é apenas palavras
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, k2d2):
      -----------    -----------    ---------
        |               |               |
        |               |               - Keyword only
        |           Positional or keyword
        -- Positional only
'''

def criar_carro(modelo, ano, placa, / marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1,0", 
            combustivel="Gasolina") # Valido

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", 
            marca="Fiat", motor="1,0", combustivel="Gasolina") #Invalido