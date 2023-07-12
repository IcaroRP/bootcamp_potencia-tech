#Isso está em loop infinito que iremos parar o com Break
'''
while True:
    opcao = int(input("Informe um número: "))

    if opcao == 10:
        break

    print(opcao)

'''

for numero in range(100):

    if numero == 12:
        continue # Ele vai pular a execução (numero 12)

    print(numero, end=" ")