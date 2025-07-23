lista = []
for peso in range(1, 6):
    p = float(input(f'Digite o peso da {peso}ª pessoa (kg): '))
    lista += [p]
print(f'\nO maior peso lido foi {max(lista)}kg e o menor foi {min(lista)}kg.')