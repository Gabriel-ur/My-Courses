print('LEITOR DE MÉDIA E MAIOR E MENOR\n')

count = 0
soma = 0
lista = []
u = ''

while u != 'n':
    n = int(input('Digite um número: '))
    u = input('Deseja continuar (\033[32ms\033[0m/\033[31mn\033[0m): ').strip().lower()
    if u != 'n' and 's':
        u = input('Resposta inválida, tente novamente (\033[32ms\033[0m/\033[31mn\033[0m): ')
    print()
    count += 1
    soma += n
    lista += [n]
print(f'\nA média entre os {count} valores que digitou é {soma / count :.2f}')
print(f'O MAIOR valor que digitou é {max(lista)}')
print(f'O MENOR valor que digitou é {min(lista)}')