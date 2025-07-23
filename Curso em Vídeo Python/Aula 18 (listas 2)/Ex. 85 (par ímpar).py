valores = [[], []]

for c in range(7):
    n = int(input(f'Digite o {c+1}° número: '))
    
    if n % 2 == 0:
        valores[0].append(n)
    elif n % 2 != 0:
        valores[1].append(n)

print(f'Os valores pares digitados foram {sorted(valores[0])}')
print(f'Os valores ímpares digitados foram {sorted(valores[1])}')