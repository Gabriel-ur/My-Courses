from unidecode import unidecode

print('-=-' * 17)
print('VERIFICADOR DE PALÍNDROMO (igual de trás pra frente)')
print('-=-' * 17)

f = unidecode(input('\nDigite uma frase/palavra: ').replace(' ', '').upper())

if f == f[::-1]:
    print('\nA frase que digitou \033[32mÉ\033[0m palíndromo.')
else:
    print(f'\nO inverso de \033[35m{f}\033[0m é \033[34m{f[::-1]}\033[0m, portanto \033[31mNÃO É\033[0m palíndromo.')