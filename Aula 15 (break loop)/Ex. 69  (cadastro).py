mais_18 = 0
homem = 0
mulher_menos_20 = 0

while True:
    print('-=-' * 6)
    print('\nCADASTRO DA PESSOA')
    print('-=-' * 6)
    print()

    i = int(input('Idade da pessoa: '))
    if i >= 18:
        mais_18 += 1

    s = input('Sexo da pessoa [\033[36mm\033[0m/\033[35mf\033[0m]: ').strip().lower()
    while s != 'm' and s != 'f':
        print('\n\033[31mSexo inválido, tente novamente\033[0m')
        s = input('Sexo da pessoa [\033[36mm\033[0m/\033[35mf\033[0m]: ').strip().lower()
    if s == 'm':
        homem += 1
    if s == 'f' and i < 20:
        mulher_menos_20 += 1

    u = input('Deseja continuar? [\033[32ms\033[0m/\033[31mn\033[0m]: ').strip().lower()
    while u != 's' and u != 'n':
        print('\n\033[31mResposta inválida, tente novamente\033[0m')
        u = input('Deseja continuar? [\033[32ms\033[0m/\033[31mn\033[0m]: ').strip().lower()
    if u == 'n':
        break

print(f'''\n>>> {mais_18} pessoas com mais de 18
>> {mulher_menos_20} mulheres com menos de 20
> {homem} homens''')