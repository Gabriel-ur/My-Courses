from datetime import date
c = 0

for nascimento in range(7):
    data = int(input('Digite o ano de nascimento (AAAA): '))
    if date.today().year - data >= 18:
        c += 1
print(f'\n{c} dessas pessoas são maiores de idade e {7-c} ainda não são.')