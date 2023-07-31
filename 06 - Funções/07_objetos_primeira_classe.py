'''
Em python tudo é objeto, dessa forma funções também são objetos
o que as tornam objetos de primeira classe. Com isso podemos
atribuir funções a variáveis, passa-las como parametros para funções,
usa-las como valores em estruturas de adados (listas, tuplas, dicionários, etc)
e usar como valor de retorno para uma função (closures)

'''

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")

exibir_resultado(10, 10, somar)
exibir_resultado(10, 10, subtrair)