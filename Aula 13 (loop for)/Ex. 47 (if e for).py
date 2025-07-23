i = int(input('Por qual número deseja começar: '))
f = int(input('Qual será o último número: '))
ip = input('Deseja ver os pares ou ímpares (\033[36mp\033[0m/\033[31mi\033[0m): ')

if ip == 'p':
    if i%2 == 0:
        for cp in range(i, f+1, 2):
            print(cp, end='; ')
    else:
        for cp in range(i+1, f+1, 2):
            print(cp, end='; ')
elif ip == 'i':
    if i%2 != 0:
        for ci in range(i, f+1, 2):
            print(ci, end='; ')
    else:
        for ci in range(i+1, f+1, 2):
            print(ci, end='; ')