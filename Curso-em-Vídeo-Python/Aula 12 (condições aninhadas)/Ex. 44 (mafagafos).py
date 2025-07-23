from unidecode import unidecode

cor = {'nd':'\033[0m','negrito':'\033[1m','italico':'\033[3m','sublinhado':'\033[4m','preto':'033[30m','vermelho':'\033[31m','verde':'\033[32m','amarelo':'\033[33m','azul':'\033[34m','roxo':'\033[35m','ciano':'\033[36m','cinza':'\033[37m','branco':'\033[97m',}

print('-=-' * 5)
print('VALOR DO PRODUTO')
print('-=-' * 5)

val = float(input('\nQual o valor do produto? R$'))
metodo1 = input('Deseja pagar à vista ou parcelado? ').lower().strip()

#cliente seleciona 'à vista"
if 'vista' in metodo1:
    met2 = unidecode(input('Deseja pagar com dinheiro, cheque ou cartão? ').lower().strip())
    if 'dinheiro' in met2 or 'cheque' in met2:
        print(f'\nO produto terá {cor["verde"]}10% de desconto{cor["nd"]}, saindo por {cor["sublinhado"]}R${val - (val * 0.1):.2f}{cor["sublinhado"]}')
    else:
        print(f'\nO produto terá {cor["amarelo"]}5% de desconto{cor["nd"]}, saindo por {cor["sublinhado"]}R${val - (val * 0.05):.2f}{cor["nd"]}')
#cliente seleciona 'parcelado'
else:
    met3 = int(input('Deseja parcelar em quantas vezes? '))
    if met3 <= 2:
        print(f'\nO produto sairá pelo mesmo valor de {cor["azul"]}R${val}{cor["nd"]}, sendo cada parcela {cor["sublinhado"]}R${val / met3:.2f}{cor["nd"]}')
    else:
        print(f'\nO produto terá {cor["vermelho"]}20% de juros{cor["nd"]}, totalizando {cor["negrito"]}R${val + (val * 0.2):.2f}{cor["nd"]}, sendo cada parcela {cor["sublinhado"]}R${(val + (val * 0.2)) / met3:.2f}{cor["nd"]}')