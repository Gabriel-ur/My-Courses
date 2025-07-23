#dicionários são variaveis compostas, ou seja, guardam mais de uma informação na memória
#a grande diferença dele pra tupla e lista é que o dicionário possui índices PERSONALIZÁVEIS

pessoas = {'nome': 'Pedro', 'idade': 43}
#o valor antes dos ':' se chama CHAVE, e ela é IMUTÁVEL

print(f'O nome é {pessoas["nome"]}')

#é possível alterar os valores de um dicionário (as chaves, não)

pessoas['nome'] = 'José'
print(f'\nAgora a pessoa é {pessoas["nome"]}')
print()

for p in pessoas: #aqui ele mostra simplesmente as chaves, sem os valores
    print(p)
print()
for p in pessoas.keys(): #dá pra fazer o mesmo com o 'keys'
    print(p)
print()
for p in pessoas.values(): #o 'values' percorre os valores da lista, apenas
    print(p)
print()
for chave, valor in pessoas.items(): #o 'items' permite mostrar tanto a chave quanto o valor
    print(chave, valor)
print()

#é possível adicionar valores e chaves ao dicionário

pessoas['altura'] = 1.76
print(pessoas) #o novo item é adicionado ao fim do dicionário
print()

#é possível remover itens do dicionário

pessoas.pop('altura') #'pop' elimina o item especificado
print(pessoas)
print()

pessoas.popitem() #'popitem' elimina o ultímo item adicionado no dicionário
print(pessoas)
print()

del pessoas['nome'] #'del' pode eliminar um item ou o dicionário por completo
print(pessoas)
print()

pessoas.clear() #o método 'clear' também funciona com dicionários, esvaziando-o por completo
print(pessoas)
print()

#é possível construir um dicionário, assim como 'tuple' e 'list'

informaçoes = []
dados = dict()

for c in range(2):
    dados['nome'] = input('Digite o nome: ').title()
    dados['idade'] = int(input('Digite a idade: '))
    dados['altura'] = float(input('Digite a altura: '))
    print()
    informaçoes.append(dados.copy()) #o 'copy' cria uma cópia do dicionário, igual o '[:]' das listas

for i in informaçoes: #'i' percorre os elementos da lista (nesse caso, são dois dicionários)
    for chave, valor in i.items(): #aqui está sendo percorrido as chaves e valores de cada dicionário 
        print(f'A chave "{chave}" recebe o valor "{valor}"\n')
print()

#assim como tuplas e listas, é possível combinar dicionários com outros dicionários ou mesmo com listas e tuplas

#aqui tem um dicionário com múltiplos dicionários dentro
pokemon = {
    '1°': {'nome': 'Pikachu', 'tipo': 'elétrico', 'considerações': 'odeio'},
    '2°': {'nome': 'Magikarp', 'tipo': 'água', 'considerações': 'nem parece...'},
    '3°': {'nome': 'Ratata', 'tipo': 'normal', 'considerações': '"é RatÁta"'},
    '4°': {'nome': 'Porygon', 'tipo': 'normal', 'considerações': 'Leon'}
}

print(pokemon['1°'])
print(pokemon['2°']['considerações'])
for p in pokemon:
    print(pokemon[p])