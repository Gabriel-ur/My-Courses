#tuplas são variaveis compostas, ou seja, guardam mais de uma informação na memória
#tuplas são IMUTÁVEIS, ou seja, não é possível mudar os elementos da variável
#normalmente são usadas para registros, guardar dados protegidos

lanche = ('batata', 'sorvete', 'suco', 'salgadinho')

print(lanche)
print(lanche[2])
print(lanche[0:2])
print(lanche[1:])
print(lanche[-1])

print()

#'enumerate' recebe duas variáveis no loop, uma mostra a posição do elemento na tupla e o outro mostra o elemento daquela posição
#ele também funciona com listas

for posiçao, comida in enumerate(lanche):
    print(f'Vou comer {comida} na posição {posiçao}')

print()
print(sorted(lanche))
print()

a = (1, 5, 7)
b = (3, 9, 1, 0)
c = b + a

print(c)
print(c.count(1))
print(c.index(1)) #retorna a primeira posição do elemento
print(c.index(1, 3)) #retorna a posição a partir do elemento na posição 3

usuario = ('Gabriel', 18, 'm', 51.50)
print()
print(usuario)
del(usuario) # del apaga uma variável