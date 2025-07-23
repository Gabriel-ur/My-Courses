from uteis import moeda

m = float(input('\nDigite um preço: \033[36mR$'))

print(f'\n\033[0mO dobro de {m} vale \033[34mR${moeda.dobro(m)}\033[0m')
print(f'A metade de {m} vale \033[35mR${moeda.metade(m):.2f}\033[0m')

p = float(input('\nQuanto deseja aumentar, em % (informe somente o n°): \033[36m'))

print(f'\033[0mO aumento de {p}% de {m} vale \033[31mR${moeda.aumento(m, p):.2f}\033[0m')

p = float(input('\nQuanto deseja diminuir, em % (informe somente o n°): \033[36m'))

print(f'\033[0mA redução de {p}% de {m} vale \033[32mR${moeda.reduz(m, p):.2f}\033[0m')