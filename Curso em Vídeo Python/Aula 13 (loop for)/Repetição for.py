# o for repete o que vc mandar, tendo mais funções além do range, também podendo colocar condições e inputs
#o for é uma "estrutura de repetição com variável de controle"
#range é um 'tipo' sequencial; existem tipos numéricos (int, float...), tipos sequenciais (lista, tupla...) e outros

#aqui, 'c' é uma variável de controle

for c in range(4, 0, -1):
    print(c)
print('Olha quantos números ao contrário\n')

for c in range(1, 8, 2):
    print(c)
print('Aqui pula de 2 em 2')

i = int(input('\nInício: '))
f = int(input('Fim: '))
p = int(input('De quanto em quanto: '))

for c in range(i, f+1, p):
    print(c)