print('-=-' * 5)
print('AUMENTO SALARIAL')
print('-=-' * 5)

sal = float(input('\nQual seu salário atual? '))

if sal >= 1250:
    print(f'\nComo seu salário é maior ou igual a R$1250,00, ele terá um aumento de 10%, passando a ser {sal+sal*0.10:.2f}')
else:
    print(f'\nComo seu salário é menor que R$1250,00, ele terá um aumento de 15%, passando a ser {sal+sal*0.15:.2f}')