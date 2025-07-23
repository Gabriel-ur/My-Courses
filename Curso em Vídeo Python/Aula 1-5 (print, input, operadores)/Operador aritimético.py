#operadores: +  -  *  /  ** (potência)  // (divisão inteira; arredonda pra baixo)  % (resto da divisão)

#ORDEM DE PRECEDÊNCIA: 
# ()
# **
# * / // %
# + -

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

print(f'A soma de {n1} e {n2} vale {n1+n2}!')
print(f'A subtração de {n1} e {n2} vale {n1-n2}!')
print(f'A multiplicação de {n1} e {n2} vale {n1*n2}!')
print(f'A divisão de {n1} e {n2} vale {n1/n2}!')
print(f'A potência de {n1} e {n2} vale {n1**n2}!')