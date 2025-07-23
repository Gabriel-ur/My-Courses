from random import randint
from time import sleep

print('-=-' * 15)
print('MEGA SENA'.center(45))
print('-=-' * 15)

jogo = [] #vai conter um único jogo
jogos = [] #vai conter todos os jogos
tot = 0

quant = int(input('Quantos jogos quer que eu sorteie: '))

while tot < quant:
    while len(jogo) != 6:
        n = randint(1, 60)
        if n not in jogo:
            jogo.append(n)
    jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()
    tot += 1

print('-' * 45)
for c in range(quant):
    print(f'{c+1}° jogo: {jogos[c]}')
    sleep(0.5)

#jeito MT MELHOR de fazer, mas n usa lista

#for c in range(int(input('Quantos jogos quer que eu sorteie: '))):
#    print(f'Jogo {c+1}: {random.sample(range(1, 61), 6)}')
#    sleep(0.5)