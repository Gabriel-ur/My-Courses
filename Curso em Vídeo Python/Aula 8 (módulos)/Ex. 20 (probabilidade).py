from random import shuffle

print('Digite o nome dos alunos e sortearei uma ordem para apresentação\n')

alu1 = input('1° aluno: ')
alu2 = input('2° aluno: ')
alu3 = input('3° aluno: ')
alu4 = input('4° aluno: ')

lista = [alu1, alu2, alu3, alu4]
shuffle(lista)

print(f'\nA ordem de apresentação é: {lista}')