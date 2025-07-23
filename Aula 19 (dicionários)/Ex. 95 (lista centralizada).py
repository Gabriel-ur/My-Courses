jogadores = []
dados = {}

while True:

    dados['Nome'] = input('Nome do jogador: ').strip().title()
    partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou: '))

    gols = []
    for c in range(1, partidas+1):
        gols.append(int(input(f'Quantos gols na {c}ª partida: ')))

    dados['Gols'] = gols
    dados['Total'] = sum(gols)

    jogadores.append(dados.copy())

    u = input('Deseja continuar? [\033[32ms\033[0m/\033[31mn\033[0m]: ').strip().lower()
    print()
    if u == 'n':
        break

print(jogadores)
print(f'{"Jogador":<12}{"Gols":<10}{"Total":>12}')
print('-' * 34)

for c, j in enumerate(jogadores):
    print(f'{c} {j["Nome"]:<10}{j["Gols"]!s:<17s}{j["Total"]!s:>1s}') #esse '!s:s' converte uma lista em str temporariamente pra conseguir centralizar
print('-' * 34)

while True:
    u = int(input('Mostrar dados de qual jogador? (999 para): '))

    while u >= len(jogadores):
        print('\033[31mERRO\033[0m, número inválido, tente novamente')
        u = int(input('Mostrar dados de qual jogador? (999 para): '))

    if u == 999:
        break

    print(f'\n>> LEVANTAMENTO DO JOGADOR {jogadores[u]["Nome"]}:')
    for c in range(len(jogadores[u]["Gols"])):
        print(f'  Na partida {c+1}, fez {jogadores[u]["Gols"][c]} gols.')
    print()