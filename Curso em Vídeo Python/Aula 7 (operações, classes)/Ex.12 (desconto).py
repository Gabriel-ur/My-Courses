print('Olá! Seja bem vindo à calculadora de descontos ;)\n')

val = float(input('Digite o valor original (em reais): '))
desc = int(input('Digite o valor do desconto (em porcentagem): '))
porcentagem = desc/100

print(f'\nO produto, após o desconto, custará {val-val*porcentagem:.2f}')