i = int(input('Por qual número deseja começar: '))
f = int(input('Qual será o último número: '))
ip = input('Deseja ver os pares ou ímpares (\033[36mp\033[0m/\033[31mi\033[0m): ')
m = int(input('Deseja ver os múltiplos de qual valor: '))

s = 0
cont = 0

if ip == 'p':
    if i%2 == 0:
        for c in range(i, f+1, 2):
             if c%m == 0:
                cont = cont + 1
                s = s + c
    else:
       for c in range(i+1, f+1, 2):
             if c%m == 0:
                cont = cont + 1
                s = s + c
elif ip == 'i':
    if i%2 != 0:
       for c in range(i, f+1):
            if c%m == 0:
                cont = cont + 1
                s = s + c
    else:
       for c in range(i+1, f+1):
            if c%m == 0:
                cont = cont + 1
                s = s + c
print(f'{cont} valores foram somados, totalizando {s}')