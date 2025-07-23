aluno = {}

aluno['nome'] = input('Nome do aluno: ').strip().title()
aluno['média'] = float(input('Média do aluno: '))

if aluno['média'] < 7:
    aluno['situação'] = '\033[31mReprovado\033[0m'
elif aluno['média'] >= 7:
    aluno['situação'] = '\033[32mAprovado\033[0m'

print(f'\nO nome do(a) aluno(a) é {aluno["nome"]}.')
print(f'A média do aluno é igual a: \033[34m{aluno["média"]:.2f}\033[0m')
print(f'A situação do aluno é {aluno["situação"]}.')