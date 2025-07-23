r = ''
while r != 'f' and r != 'm':
    r = input('Digite o sexo do indivíduo (\033[36mm\033[0m/\033[31mf\033[0m): ').lower().strip()
    if r != 'f' and r != 'm':
        print('\033[31mERRO\033[0m')
print(f'\nA pessoa tem o sexo {r}')