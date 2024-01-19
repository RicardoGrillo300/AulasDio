menu = '''
    ============ BANCO LOCAL ============
    
    1 - Deposito
    2 - Saque
    3 - Extrato
    4 - Sair
    
    =====================================
'''

print(menu)

saldo_conta = 0
saque = []
depositos = []
limite_saque = 3
cont = 0

while True:
    
    escolha = int(input('Digite sua opcao: '))
    
    if escolha == 1:
        print('=' * 37)
        valor_deposito = float(input('Digite o valor a ser depositado: R$'))
        if valor_deposito > 0:
            saldo_conta += valor_deposito
            print(f'foi depositado o valor de R$ {valor_deposito:.2f}')
            print('=' * 37)
            depositos.append(valor_deposito)
        else: 
            print('Deposito deve ser superior a R$ 0,00')
    elif escolha == 2:
        print('=' * 37)
        if saldo_conta > 0:
            if limite_saque > 0:
                valor_saque = float(input('Digite o valor para o saque: R$'))
                if valor_saque > 0:
                    if valor_saque <= saldo_conta:
                        if valor_saque > 500:
                            print('O limite de saque é de apenas R$ 500,00')
                        else:
                            print(f'Retire o valor de R$ {valor_saque:.2f} na boca do caixa')
                            saldo_conta -= valor_saque
                            limite_saque -= 1
                            saque.append(valor_saque)
                            print('=' * 37)
                    else:
                        print(f'Operação invalida! O valor R$ {valor_saque:.2f} é maior do que o saldo em conta!')
                        print('=' * 37)
            else:
                print('Você excedeu o limite de saque diário!')
        else:
            print('Operação invalida! Você não possui saldo na sua conta!')
            print('=' * 37)
    elif escolha == 3:
        print('=' * 37)
        print('EXTRATO'.center(37))
        print('-' * 37)
        if len(saque) > 0:
            print('SAIDAS'.center(37))
            for saida in saque:
                print(f'Saque: R$ {saida:.2f}\n')
        elif len(saque) >= 0:
                print('\n')
        if len(depositos) > 0:
            print('ENTRADAS'.center(37))
            for entradas in depositos:
                print(f'Depósito: R$ {entradas:.2f}\n')
        elif len(depositos) <= 0:
            print('\n')
        print('-' * 37)
        print(f'Saldo disponível: R$ {saldo_conta:.2f}')
        print('=' * 37)
    elif escolha == 4:
        print('=' * 37)
        print('Obrigado por usar o BANCO LOCAL!')
        print('=' * 37)
        break
    else:
        print('Opcao invalida!')