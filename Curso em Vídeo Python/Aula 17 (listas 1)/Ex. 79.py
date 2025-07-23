valores = list()

while True:
    num = int(input('Digite um número: '))
    if num not in valores:
        valores.append(num)
    else:
        print('valor duplicado')
    u = input('\nDeseja continuar? [\033[32ms\033[0m/\033[31mn\033[0m]: ').strip().lower()
    if u == 'n':
        break

print(f'\nVocê digitou os valores {sorted(valores)}')