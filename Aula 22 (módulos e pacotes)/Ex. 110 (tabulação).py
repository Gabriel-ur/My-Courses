from uteis import moeda2

m = float(input('Digite um preço: R$'))
a = float(input('Quanto deseja aumentar, em % (informe somente o n°): '))
d = float(input('Quanto deseja diminuir, em % (informe somente o n°): '))

print()
moeda2.resumo(m, a, d)