dados = []

while True:
    nome = input('Nome: ').strip().title()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 1: '))

    dados.append([nome, [nota1, nota2], (nota1 + nota2) / 2])

    u = input('Deseja continuar? [\033[32mS\033[0m/\033[31mN\033[0m]: ').strip().lower()
    print('-=-' * 9)
    if u == 'n':
        break

print(f'{"N°":<8}{"Nome":<10}{"Média":>9}')
print('-' * 27)

for c, aluno in enumerate(dados):
    print(f'{c:<8}{aluno[0]:<10}{aluno[2]:>9}')

while True:
    print('-' * 27)
    u = int(input('Mostrar a nota de qual aluno? (999 interrompe): ').strip().title())
    if u == 999 or u >= len(dados):
        break
    print(f'As notas de {dados[u][0]} são {dados[u][1]}')

print(dados)