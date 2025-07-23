n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 > n2:
    print(f'\nO primeiro n° (\033[34m{n1}\033[0m) é maior que o segundo (\033[31m{n2}\033[0m)')
elif n2 > n1:
    print(f'\nO segundo n° (\033[34m{n2}\033[0m) é maior que o primeiro (\033[31m{n1}\033[0m)')
else:
    print(f'\nAmbos os números (\033[35m{n1}, {n2}\033[0m) são iguais.')