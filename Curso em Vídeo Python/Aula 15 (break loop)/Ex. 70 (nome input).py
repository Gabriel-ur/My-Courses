soma = 0
p_mais_1000 = 0
nome_barato = ''
cont = 0
menor_val = 0

while True:
    nome_p = input('Nome do produto: ').strip().title()

    val = float(input('Preço: \033[32mR$'))
    soma += val
    if val > 1000:
        p_mais_1000 += 1
        
    cont += 1
    if cont == 1 or val < menor_val:
        menor_val = val
        nome_barato = nome_p
#esse else aqui embaixo não é necessário porque os blocos são iguais
    #else:
    #    if val < menor_val:
    #        menor_val = val
    #        nome_barato = nome_p

    u = input('\033[0mDeseja continuar? [\033[32ms\033[0m/\033[31mn\033[0m]: ').strip().lower()
    while u != 's' and u != 'n':
        print('\n\033[31mResposta inválida, tente novamente\033[0m')
        u = input('Deseja continuar? [\033[32ms\033[0m/\033[31mn\033[0m]: ').strip().lower()
    print()
    if u == 'n':
        break

print(f'''Total da compra: \033[32mR${soma:.2f}\033[0m
Total de produtos por mais de R$1000.00: \033[31m{p_mais_1000}\033[0m
O produto mais barato é "{nome_barato}" e vale R${menor_val:.2f}''')