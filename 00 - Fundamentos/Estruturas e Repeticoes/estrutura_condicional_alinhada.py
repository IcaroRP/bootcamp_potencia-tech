conta_normal = False
conta_universitaria = True

saldo = 2000
saque = 500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print('Saque realizado com sucesso! (Conta normal)')
    elif saque <= (saldo + cheque_especial):
        print('Saque realizado com uso do chegue especial. (Conta normal)')
    else:
        print('Não foi possivel realizar a operação.')    
elif conta_universitaria:
    if saldo >= saque:
        print('Saque realizado com sucesso! (Conta universitaria)')
    else:
        print('Saldo insuficiente (Conta universitaria)')
else:
    print('Sistema não reconheceu o seu tipo de conta. Por favor, entre em contato com o gerente')
    