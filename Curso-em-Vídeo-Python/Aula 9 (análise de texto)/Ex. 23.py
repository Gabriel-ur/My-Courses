#uma pouca vergonha esse exercício

n = int(input('Digite um número entre 0 e 9999: '))

print('\nAnalisando o número...\n')

print(f'Unidade: {n // 1 % 10}')
print(f'Dezena: {n // 10 % 10}')
print(f'Centena: {n // 100 % 10}')
print(f'Milhar: {n // 1000 % 10}')