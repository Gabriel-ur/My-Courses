#criar uma lista com 5 palavras
#selecionar uma palavra aleatória da lista
#dar 6 chances pro usuário adivinhar uma letra da palavra
#perguntar qual letra o usuário quer adivinhar
#mostrar as letras que o usuário já adivinhou
#mostrar as letras que o usuário já errou

import random, time

possiveis_palavras = ['preto', 'branco', 'azul', 'verde', 'vermelho', 'roxo', 'amarelo', 'laranja', 'cinza', 'ciano']

print('Bem-vindo ao jogo da forca!')
print('Tente adivinhar a palavra abaixo:')

palavra = random.choice(possiveis_palavras)

palavra_oculta = ['_' for letra in palavra]
chances = 6
letras_erradas = []

while chances != 0:
    print('')
    print(' '.join(palavra_oculta))
    print(f'\nChances restantes: {chances}')
    print(f'Letras erradas: {' '.join(letras_erradas)}')
    letra = input('\nDigite uma letra: ').lower().strip()
    if letra in palavra:
        for i, l in enumerate(palavra):
            if l == letra:
                palavra_oculta[i] = letra
    elif letra in letras_erradas:
        print(f'\nVocê já tentou a letra \033[31m{letra}\033[0m. Tente outra!')
        time.sleep(2)
        continue
    else:
        chances -= 1
        letras_erradas.append(letra)
    if '_' not in palavra_oculta:
        print(f'\n\033[32mParabéns!\033[0m Você adivinhou a palavra: \033[1m{palavra}\033[0m')
        break
    if chances == 0:
        print(f'\n\033[31mVocê perdeu!\033[0m A palavra era: \033[1m{palavra}\033[0m')
        break
