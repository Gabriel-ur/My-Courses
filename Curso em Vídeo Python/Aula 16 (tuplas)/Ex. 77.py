palavras = ('cachorro', 'Jorge', 'beringela', 'leite', 'limonada',
            'soro', 'escada', 'urangutango', 'escada', 'docente',
            'livro', 'papel', 'desgraça', 'rancor', 'tristeza')

for p in palavras:
    print(f'\nA palavra {p.upper()} possui as vogais ', end='')
    for vogal in p:
        if vogal in 'aeiou':
            print(vogal.lower(), end=' ')
    print()