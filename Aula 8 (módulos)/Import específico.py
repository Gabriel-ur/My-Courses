#a sintaxe abaixo serve para importar funções específicas de um módulo, sem a necessidade de importá-lo por inteiro. Isso ajuda a não deixar o programa desnecessariamente pesado

from math import sqrt

numero = int(input('Digite um número: '))
raiz = sqrt(numero)

print(f'A raiz quadrada de {numero} é {raiz:.0f}')