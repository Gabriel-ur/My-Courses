from time import sleep

n1 = int(input('Digite um 1º valor: '))
n2 = int(input('Digite um 2º valor: '))
u = 0

while u != 5:
    print('\n>>> Você deseja...')
    print('\n[ 1 ] somá-los')
    print('[ 2 ] multiplicá-los')
    print('[ 3 ] ver qual é o maior')
    print('[ 4 ] digitar novos números')
    print('[ 5 ] sair do programa')
    u = int(input('\n:: '))
    if u == 1:
        print(f'\nA soma de {n1} e {n2} é igual a {n1+n2}')
        sleep(2)
    elif u == 2:
        print(f'\nA multiplicação de {n1} e {n2} é igual a {n1*n2}')
        sleep(2)
    elif u == 3:
        if n1 > n2:
            print(f'\n{n1} é maior que {n2}')
            sleep(1.5)
        elif n2 > n1:
            print(f'\n{n2} é maior que {n1}')
            sleep(1.5)
        else:
            print(f'\nAmbos os valores que digitou são iguais.')
            sleep(1.5)
    elif u == 4:
        print('\nOk, digite os novos valores abaixo.')
        n1 = int(input('Digite um 1º valor: '))
        n2 = int(input('Digite um 2º valor: '))
    elif u != 5:
        print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE.\n')
        sleep(2)
    else:
        print('\nFINALIZANDO...')
        sleep(2)
        print('=-' * 20)