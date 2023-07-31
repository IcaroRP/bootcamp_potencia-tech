'''
Podemos combinar parâmetros obrigatórios com args e kwargs.
Quando esses são definidos (*args e **kwargs), o metodo recebe
os valores como tupla e dicionário respectivamento.

'''

def exibir_poema(data_extenso, *lista, **dicionario):
    texto = "\n".join(lista)
    
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in dicionario.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("Sexta-Feira, 26 de Agosto de 2022", 
             "Zen of Python", 
             "Beautiful is better than ugly.", 
             autor="Tim Peters", 
             ano=1999
             )