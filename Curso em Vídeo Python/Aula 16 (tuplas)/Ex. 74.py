from random import choices

numeros = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

pc = choices(numeros, k=5)

print(f'Os valores sorteados foram: {pc}')
print(f'O maior valor é {max(pc)}')
print(f'O menor valor é {min(pc)}')