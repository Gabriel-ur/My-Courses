print('Esse programa dirá qual seu reajuste salarial (ajuste para melhor ;^)\n')

sal = float(input('Seu salário original: '))
aumen = int(input('O reajuste (em porcentagem): '))
porcentagem = aumen/100

print(f'\nSeu salário, após o ajuste, passará a ser de R${sal+sal*porcentagem:.2f}')