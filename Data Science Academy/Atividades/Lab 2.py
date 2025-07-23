print('-' * 15, 'Calculadora em Python', '-' * 15)

print('Selecione o número da operação desejada:\n')

print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')

while True:
    try:
        operacao = int(input('\n\033[32mDigite sua opção (1/2/3/4): \033[0m'))
    except:
        print('\033[31mOpção inválida! Digite novamente.\033[0m')
        continue
    if operacao not in [1, 2, 3, 4]:
        print('\033[31mOpção inválida! Digite novamente.\033[0m')
    else:
        break

while True:
    try:
        num1 = float(input('\n\033[34mDigite o primeiro número: \033[0m'))
    except:
        print('\033[31mOpção inválida! Digite novamente.\033[0m')
    else:
        break

while True:
    try:
        num2 = float(input('\n\033[34mDigite o segundo número: \033[0m'))
    except:
        print('\033[31mOpção inválida! Digite novamente.\033[0m')
    else:
        break

if operacao == 1:
    print(f'\n{num1} + {num2} = {num1 + num2}')
if operacao == 2:
    print(f'\n{num1} - {num2} = {num1 - num2}')
if operacao == 3:
    print(f'\n{num1} * {num2} = {num1 * num2}')
if operacao == 4:
    print(f'\n{num1} / {num2} = {num1 / num2}')