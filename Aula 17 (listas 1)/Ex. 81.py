valores = []

while True:
    n = int(input('\nDigite um número: '))
    if n not in valores:
        valores.append(n)
    else:
        print('\033[31mO valor que digitou já foi adicionado\033[0m')
    u = input('Deseja continuar? [\033[32ms\033[0m/\033[31mn\033[0m]: ').strip().lower()
    if u == 'n':
        break

print(f'''\nForam digitados {len(valores)} números
Os valores que digitou, em ordem decrescente: {sorted(valores, reverse = True)}''')
print('O n° 5 foi digitado' if 5 in valores else 'O n° 5 não foi digitado')
