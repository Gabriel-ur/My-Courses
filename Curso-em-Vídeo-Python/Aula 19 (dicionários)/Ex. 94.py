pessoas = []
dados = {}
soma = media = 0

while True:
    dados['nome'] = input('Nome: ').strip().title()
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']

    s = input('Sexo [\033[36mm\033[0m/\033[35mf\033[0m]: ').strip().lower()

    while s != 'm' and s != 'f':
        print('\n\033[31mSexo inválido, tente novamente\033[0m')
        s = input('Sexo da pessoa [\033[36mm\033[0m/\033[35mf\033[0m]: ').strip().lower()

    dados['sexo'] = s

    pessoas.append(dados.copy())

    u = input('Deseja continuar? [\033[32ms\033[0m/\033[31mn\033[0m]: ').strip().lower()
    print()
    if u == 'n':
        break

print(pessoas)
print('-=' * 25)

print(f'\nO grupo tem {len(pessoas)} pessoas.')
print(f'A média das idades é {soma / len(pessoas):.2f} anos.')

print('As mulheres cadastradas são: ', end='')
for p in pessoas:
    if p['sexo'] == 'f':
        print(f'{p["nome"]}', end='; ')

print('\n\nPessoas que estão acima da média de idade:')
for p in pessoas:
    if p['idade'] >= soma / len(pessoas):
        print('>> ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()