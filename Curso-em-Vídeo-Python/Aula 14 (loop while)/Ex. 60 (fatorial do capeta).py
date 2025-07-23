print('LEITOR DE FATORIAL')

n = int(input('\nDigite um número inteiro e positivo: '))
c = n
#o valor neutro para multiplicação é 1, por isso esse 'f' é 1
f = 1
print(f'{n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)