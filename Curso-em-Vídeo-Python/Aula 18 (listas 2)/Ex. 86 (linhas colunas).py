matriz = [[0,0,0], [0,0,0], [0,0,0]]

for linha in range(3):
    for coluna in range(3): #todas as colunas de uma linha vão ser contadas antes da próxima linha
        matriz[linha][coluna] = int(input(f'Digite o número para [{linha}, {coluna}]: '))

print()
for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print() #toda vez que todas as colunas da linha sofrerem print, quebra ao mudar de linha