#é possível colocar listas dentro de listas

dados = ['Gabriel', 18]

pessoas = []
pessoas.append(dados[:]) #esse '[:]' cria uma cópia da lista original

pessoas = [['Gabriel', 18], ['Tamires', 21], ['Maycon', 23]]

print(pessoas)
print()
print(pessoas[0][1])
print(pessoas[1][0])
print(pessoas[2][1])
print(pessoas[0])
print()

for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos')
print()

galera = []
dados = []
for c in range(3):
    dados.append(input('Nome: ').title())
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()
print()
print(galera)
    