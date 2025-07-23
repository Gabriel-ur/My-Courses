from random import randint
import emoji

print('-=-' * 7)
print('ADIVINHAÇÃO APRIMORADA')
print('-=-' * 7)
print('''Vou escolher um número de 0 a 10...
será que você adivinha qual é? 🧐''')

u = int(input('\nSeu palpite: '))
pc = randint(0, 10)
tent = 1

while pc != u:
    print('haha, você errou >: tente novamente')
    if pc < u:
        print(f'\nAqui vai uma dica... o número que escolhi é MENOR que {u}')
    elif pc > u:
        print(f'\nAqui vai uma dica... o número que escolhi é MAIOR que {u}')
    u = int(input('\nSeu...NOVO palpite 🤭: '))
    tent += 1

if tent == 1:
    print(f'\nParabêns, você ganhou.')
elif tent >= 1:
    print(f'\nParabêns, você ganhou (depois de {tent} tentativas, mas tudo bem 😏).')