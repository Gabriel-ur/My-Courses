from random import randint

print('-=-' * 4)
print('PAR OU ÍMPAR')
print('-=-' * 4)

count = 0

while True:
    n = int(input('Digite um número: '))
    ip = input('Par ou ímpar? [\033[35mp\033[0m/\033[36mi\033[0m]: ').strip().lower()

    while ip != 'p' and 'i':
            print('\n\033[31mJogada inválida, tente novamente\033[0m')
            ip = input('Par ou ímpar? [\033[35mp\033[0m/\033[36mi\033[0m]: ').strip().lower()

    pc = randint(1, 10)
    resto = (pc + n) % 2

    print(f'\nVocê jogou {n} e o computador jogou {pc}. Total de {n + pc} ', end = '')

    if resto == 0 and ip == 'p':
        print('Deu \033[4mPAR\033[0m \n\033[32mVocê GANHOU\033[0m\n')
        print('Vamos de novo...\n')
        count += 1
    elif resto == 0 and ip == 'i':
        print('Deu \033[4mPAR\033[0m \n\033[31mVocê PERDEU\033[0m\n')
        break
    elif resto != 0 and ip == 'i':
        print('Deu \033[4mÍMPAR\033[0m \n\033[32mVocê GANHOU\033[0m\n')
        print('Vamos de novo...\n')
        count += 1
    elif resto != 0 and ip == 'p':
        print('Deu \033[4mÍMPAR\033[0m \n\033[31mVocê PERDEU\033[0m\n')
        break

print(f'Jogo finalizado. Você ganhou {count} vezes.')