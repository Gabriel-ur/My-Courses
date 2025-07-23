print('-=-' * 5)
print('MY HOUSE MY LIFE')
print('-=-' * 5)

casa = float(input('\nQual o valor da casa que deseja comprar? R$'))
salario = float(input('Qual seu salário? R$'))
anos = int(input('Em quantos anos deseja pagar? '))

prestaçao = casa / (anos * 12)

if prestaçao < salario * 0.3:
    print(f'\n\033[36mPARABÉNS!!!\033[0m, seu empréstimo foi bem sucedido e a prestação será de R${prestaçao:.2f} ;)')
else:
    print(f'\n\033[31mPoxa...\033[0m infelizmente seu empréstimo foi negado... mas a prestação SERIA de R${prestaçao:.2f} :)')