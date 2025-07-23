valores = []
pares = []
impares = []

while True:
    n = int(input('\nDigite um número: '))
    if n not in valores:
        valores.append(n)
    else:
        print('\033[31mO valor que digitou já foi adicionado\033[0m')
    if n % 2 == 0:
        pares.append(n)
    elif n % 2 != 0:
        impares.append(n)
    u = input('Deseja continuar? [\033[32mS\033[0m/\033[31mN\033[0m]: ').strip().lower()
    if u == 'n':
        break

print(f'''\nTodos os valores que digitou: {sorted(valores)}
Apenas os números pares: {sorted(pares)}
Apenas os números ímpares: {sorted(impares)}''')
