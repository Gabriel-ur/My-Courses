from unidecode import unidecode

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for p in range(1, 5):
    n = unidecode(input(f'Digite o nome da {p}ª pessoa: ')).strip().upper()
    i = int(input(f'Digite a idade da {p}ª pessoa: '))
    s = input(f'Digite o sexo da {p}ª pessoa (\033[36mm\033[0m/\033[31mf\033[0m): ')
    print()
    somaidade += i
    if p == 1 and s == 'm':
        maioridadehomem = i
        nomevelho = n
    if s == 'f' and i < 20:
        totmulher20 += 1
mediaidade = somaidade/4

print(f'A média da idade dos indivíduos é {mediaidade}')
print(f'O homem mais velho tem {maioridadehomem} anos e seu nome é {nomevelho}.')
print(f'Ao todo são {totmulher20} mulher(es) com menos de 20 anos.') 