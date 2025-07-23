#condição aninhada é quando tem mais de uma possibilidade dentro de uma condição

n = int(input('Escolha um número de 0 a 9: '))

if n == 1 or n == 3 or n == 7 or n == 9:
    print(f'\nPuts, eu não gosto muito do {n} :/')
elif n == 6:
    print(f'\nNossa, o {n} é meu número preferido :o')
else:
    print(f'\nCaramba, eu acho o {n} bem legal :)')