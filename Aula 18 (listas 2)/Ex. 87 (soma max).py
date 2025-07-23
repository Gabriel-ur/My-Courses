matriz = [[0,0,0], [0,0,0], [0,0,0]]
soma_par = soma_col = 0

for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f'Digite o número para [{linha}, {coluna}]: '))

        if matriz[linha][coluna] % 2 == 0:
            soma_par += matriz[linha][coluna]
        if coluna == 2:
            soma_col += matriz[linha][coluna]

print()
for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()

print(f'\nA soma dos números pares é {soma_par}')
print(f'A soma dos n° da 3ª coluna é {soma_col}')
print(f'O maior valor da 2ª linha é {max(matriz[1])}')