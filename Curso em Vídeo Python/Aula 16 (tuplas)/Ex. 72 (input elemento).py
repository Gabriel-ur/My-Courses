numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input('\nDigite um número de 0 a 20: '))

    while n not in range(0, 21):
        print('\n\033[31mNÚMERO INVÁLIDO, tente novamente\033[0m')
        n = int(input('Digite um número de 0 a 20: '))

    print(f'\nVocê digitou o número \033[32m{numeros[n]}\033[0m.')
    
    u = input('Deseja continuar? [\033[32ms\033[0m/\033[31mn\033[0m]: ').strip().lower()
    while u != 's' and u != 'n':
        print('\n\033[31mResposta inválida, tente novamente\033[0m')
        u = input('Deseja continuar? [\033[32ms\033[0m/\033[31mn\033[0m]: ').strip().lower()
    if u == 'n':
        break