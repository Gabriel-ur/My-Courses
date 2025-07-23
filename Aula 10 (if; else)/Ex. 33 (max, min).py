n1 = int(input('1° valor: '))
n2 = int(input('2° valor: '))
n3 = int(input('3° valor: '))

lista = [n1, n2, n3]

print(f'''\nO maior número é \033[32m{max(lista)}\033[0m
O menor número é \033[31m{min(lista)}\033[0m''')