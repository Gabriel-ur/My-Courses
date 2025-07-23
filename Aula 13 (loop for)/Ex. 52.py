n = int(input('Digite um número: '))
t = 0

for c in range(1, n+1):
    if n%c == 0:
        print('\033[31m', end=' ')
        t += 1
    else:
        print('\033[34m', end=' ')
    print(c, end='')

if t == 2:
    print(f'\n\033[0mO número {n} é primo.')
else:
    print(f'\n\033[0mO número {n} não é primo, pois ele é divisível por {t} valores.')