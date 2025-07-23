valores = list(int(input(f'Digite um número na posição {val}: ')) for val in range(5))

print(f'\nO maior valor digitado foi {max(valores)} e o menor foi {min(valores)}')

print('O menor número está na posição: ', end='')
for pos, val in enumerate(valores):
    if min(valores) == val:
        print(pos, end='; ')

print('\nO maior número está na posição: ', end='')
for pos, val in enumerate(valores):
    if max(valores) == val:
        print(pos, end='; ')