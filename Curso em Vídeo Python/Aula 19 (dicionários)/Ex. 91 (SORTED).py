from random import randint
from time import sleep

jogadores = {}

for c in range(1, 5):
    jogadores[f'jogador {c}'] = randint(1, 6)

sleep(0.5)
print('Valores sorteados:')
print()

for chave, valor in jogadores.items():
    print(f'O {chave} tirou \033[1m{valor}\033[0m')
    sleep(0.8)

print('-=-' * 7)
print('Ranking dos jogadores:')
print()
sleep(0.8)

#'sorted' ordena o dicionário criando uma LISTA com TUPLAS
#o 'dict' aqui serve pra criar uma lista ordenada
#o 'item[1]' serve pra mostrar os valores; caso quisesse as chaves, 'item[0]'
#o 'reverse' é pra ordenar de trás pra frente

ordenado = dict(sorted(jogadores.items(), key=lambda item: item[1], reverse=True))
n = 1

for chave, valor in ordenado.items():
    print(f'{n}° lugar: \033[1m{chave}\033[0m com {valor}')
    sleep(0.8)
    n +=1