def area(l, c):
    return l * c


print('-=-' * 12)
print('CÁLC. DA ÁREA DE TERRENO \033[31mRETANGULAR\033[0m')
print('-=-' * 12)

larg = float(input('\nQual a largura do terreno (m): '))
comp = float(input('Qual o comprimento do terreno (m): '))

print(f'\nA área de um terreno \033[36m{larg} x {comp}\033[0m vale \033[32m{area(larg, comp):.2f}m²\033[0m')