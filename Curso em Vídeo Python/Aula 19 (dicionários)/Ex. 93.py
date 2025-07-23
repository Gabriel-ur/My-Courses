dados = {}

dados['Nome'] = input('Nome do jogador: ').strip().title()
partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou: '))

gols = []
for c in range(1, partidas+1):
    gols.append(int(input(f'Quantos gols na {c}ª partida: ')))

dados['Gols'] = gols
dados['Total'] = sum(gols)

print()
for chave, valor in dados.items():
    print(f'{chave} tem o valor {valor}')

print(f'\nO jogador {dados["Nome"]} jogou {partidas} partidas.\n')

for c in range(partidas):
    print(f'   -> Na partida {c+1}, fez {gols[c]} gols.')

print(f'\nFoi um total de \033[32m{dados["Total"]}\033[0m gols.')