pessoas = []
dados = []
maior = menor = 0

while True:
    dados.append(input('\nNome: ').title().strip())
    dados.append(float(input('Peso (kg): ')))

    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]

    pessoas.append(dados[:])
    dados.clear()

    u = input('Deseja continuar? [\033[32mS\033[0m/\033[31mN\033[0m: ').strip().lower()
    if u == 'n':
        break

print(f'\nForam cadastradas {len(pessoas)} pessoas.')
for nome, peso in pessoas:
    if peso == maior:
        print(f'O maior peso foi {maior}kg de {nome}')
for nome, peso in pessoas:
    if peso == menor:
        print(f'O menor peso foi {menor}kg de {nome}')