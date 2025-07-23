from uteis import moeda

m = float(input('\nDigite um preço: R$'))

print(f'\nO dobro de {moeda.moeda(m)} vale \033[34m{moeda.moeda(moeda.dobro(m))}\033[0m')
print(f'A metade de {moeda.moeda(m)} vale \033[35m{moeda.moeda(moeda.metade(m))}\033[0m')

p = float(input('\nQuanto deseja aumentar, em % (informe somente o n°): \033[36m'))

print(f'\033[0mO aumento de {p}% de {moeda.moeda(m)} vale \033[31m{moeda.moeda(moeda.aumento(m, p))}\033[0m')

p = float(input('\nQuanto deseja diminuir, em % (informe somente o n°): \033[36m'))

print(f'\033[0mA redução de {p}% de {moeda.moeda(m)} vale \033[32m{moeda.moeda(moeda.reduz(m, p))}\033[0m')