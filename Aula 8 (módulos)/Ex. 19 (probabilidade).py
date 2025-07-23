#random é um módulo interno do python que serve para lidar com probabilidade

from random import choice

n1 = input('Número: ')
n2 = input('Número: ')
n3 = input('Número: ')
n4 = input('Número: ')
n5 = input('Número: ')

lista = [n1,n2,n3,n4,n5]
sorteado = choice(lista)

print(f'\nO número sorteado foi: {sorteado}')