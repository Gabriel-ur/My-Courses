def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except:
            print('\033[31mERRO. O valor que digitou é inválido, tente novamente.\033[0m')
        else:
            return n


def menu(lista):
    print('MENU PRINCIPAL'.center(30))
    print('-' * 30)

    c = 1
    for item in lista:
        print(f'\033[32m{c} - \033[34m{item}\033[0m')
        c += 1
    print('-' * 30)
    
    u = leiaInt('\033[32mSua opção: \033[0m')
    while u not in range(1, 4):
        print('\033[31mERRO. Opção inválida, tente novamente.\033[0m')
        u = int(input('\033[32mSua opção: \033[0m'))
    return u