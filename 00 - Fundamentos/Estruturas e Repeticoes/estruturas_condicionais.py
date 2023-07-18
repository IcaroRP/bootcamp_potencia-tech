MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

idade = int(input('Informe a sua idade: '))

'''IF'''
if idade >= MAIOR_IDADE:
    print('Você é maior de idade. Pode retirar o seu CNH')

if idade <= MAIOR_IDADE:
    print('Você é menor de idade. Ainda não pode retirar o seu CNH')


'''IF-ELSE'''
if idade >= MAIOR_IDADE:
    print('Você é maior de idade. Pode retirar o seu CNH')
else:
    print('Você é menor de idade. Ainda não pode retirar o seu CNH')


'''IF-ELIF'''
if idade >= MAIOR_IDADE:
    print('Maior de idade, pode tirar a CNH')
elif idade == IDADE_ESPECIAL:
    print('Pode fazer aulas teóricas, mas não pode fazer aulas práticas')
else:
    print('Ainda não pode tirar a CNH')    