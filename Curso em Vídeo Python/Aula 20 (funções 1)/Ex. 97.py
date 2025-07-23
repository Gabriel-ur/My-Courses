def escreva(txt):
    print('=' * (len(txt) + 2))
    print(txt.center(len(txt) + 2))
    print('=' * (len(txt) + 2))


while True:
    txt = input('Digite um texto: ').title().strip()
    print()
    escreva(txt)
    u = input('Deseja continuar? [\033[32mS\033[0m/\033[31mN\033[0m]: ').strip().lower()
    if u == 'n':
        break

print('\n\033[32mTchau :)\033[0m')