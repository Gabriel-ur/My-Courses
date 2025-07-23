from random import randint

print('-=-' * 17)
print('Pensarei em um número de 0 a 5... Tente adivinhar!')
print('-=-' * 17)

escolha = int(input('\nQual número acha que escolhi >:)? '))
n = randint(0, 5)
print('\033[97;42mPROCESSANDO...\033[0m')

if escolha == n:
    print('\nSafado, não é que acertou')
else:
    print(f'\nKKKK, ganhei, o número {n} é muito melhor que esse seu {escolha}')