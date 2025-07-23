from datetime import date

dados = {}

dados['Nome'] = input('Digite seu nome: ').strip().title()
nascimento = int(input('Ano de nascimento: '))
dados['Idade'] = date.today().year - nascimento
dados['CTPS'] = int(input('Carteira de trabalho (0 se não tiver): '))

if dados['CTPS'] != 0:

    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: \033[32mR$'))
    dados['Aposentadoria'] = dados['Contratação'] - nascimento + 35

print()
for chave, valor in dados.items():
    print(f'\033[0m{chave} tem valor {valor}')
