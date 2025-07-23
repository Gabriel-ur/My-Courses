from uteis import moeda2, validaçao

m = validaçao.validaçao('Digite um preço: R$')
a = validaçao.validaçao('Quanto deseja aumentar, em % (informe somente o n°): ')
d = validaçao.validaçao('Quanto deseja diminuir, em % (informe somente o n°): ')

print()
moeda2.resumo(m, a, d)