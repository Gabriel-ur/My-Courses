def ficha(n, g):

    if not n:
        n = '<desconhecido>'
    if g.isnumeric():
        g = int(g)
    else:
        g = 0

    print(f'O jogador {n} fez {g} gol(s).')


nome = input('Nome do jogador: ').title()
gols = input('Quantidade de gols: ')

ficha(nome, gols)