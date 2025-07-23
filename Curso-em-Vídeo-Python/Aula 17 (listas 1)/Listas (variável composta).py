#listas são variaveis compostas, ou seja, guardam mais de uma informação na memória
#diferentemente das tuplas, as listas PODEM ser alteradas

nome = ['G', 'a', 'b', 'r', 'i', 'e', 'l']

print(nome)
print(len(nome))
print(''.join(nome))
print(nome[1:6])
print(nome[-7:7:2])
print()

escola = ['caderno', 'apostila', 'lápis', 'borracha', 'caneta', 'estojo']
print(escola[:3])

#aqui o elemento do indice 2 foi alterado na lista original
escola[2]= 'lapiseira'
print(escola[:3])
print()

#aqui são métodos de adicionar elementos à lista original, alterando-a

escola += ['mochila', 'corretivo'] #elementos foram adicionados ao fim da lista original
print(escola)

escola.append(':)') #elemento está sendo adicionado, mas apenas 1 pode ser adicionado por vez
print(escola)

escola.extend([10, 6]) #elementos sendo adicionados, porém mais de 1 é possível ao mesmo tempo, igual o "+= []" de cima, porém simplificado
print(escola)

escola.insert(0, 'Hello') #o insert serve pra adicionar um elemento numa posição específica
print(escola) 
print()

#aqui são metodos de eliminar elementos

del escola[6] #remove o elemento do INDÍCE declarado
print(escola)

escola.remove(6) #remove o elemento em específico
escola.remove(10) #caso o elemento aparecer mais de uma vez, elimina a primeira ocorrência apenas
print(escola)

escola.pop() #remove o último elemento da lista
print(escola)

escola.clear() #clear limpa a lista, sem deleta-la da existência, apenas tira seus elementos
print(escola)
print()

#o método 'list', igual 'tuple' das tuplas, cria uma lista
num = list(int(input('Digite um valor: ')) for n in range(4))
print(num)
print()

#métodos para ordenar os elementos de listas

letras = ['a', 'j', 'k', 'e', 'y', 'l', 'u']
letras.sort()
print(letras) #'sort' modifica a lista original, colocando-a em ordem

print(sorted(letras)) #'sorted' cria uma nova lista e coloca ela em ordem, sem modificar a original
print(sorted(letras, reverse = True)) #aqui a mesma coisa, porém com a ordem ao contrário
