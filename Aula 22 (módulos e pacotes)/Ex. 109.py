from uteis import moeda2

m = float(input('\nDigite um preço: R$'))

print(f'\nO dobro de {moeda2.moeda(m)} vale \033[34m{moeda2.dobro(m, True)}\033[0m')
print(f'A metade de {moeda2.moeda(m)} vale \033[35m{moeda2.metade(m, True)}\033[0m')

p = float(input('\nQuanto deseja aumentar, em % (informe somente o n°): \033[36m'))

print(f'\033[0mO aumento de {p}% de {moeda2.moeda(m)} vale \033[31m{moeda2.aumento(m, p, True)}\033[0m')

p = float(input('\nQuanto deseja diminuir, em % (informe somente o n°): \033[36m'))

print(f'\033[0mA redução de {p}% de {moeda2.moeda(m)} vale \033[32m{moeda2.reduz(m, p, True)}\033[0m')