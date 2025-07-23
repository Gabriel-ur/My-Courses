print('-=-' * 6)
print('PAR OU ÍMPAR? :O')
print('-=-' * 6)

n = int(input('\nDigite um número: '))

if n % 2 == 0:
    print('\nO número que você escolheu é \033[4mpar')
else:
    print('\nO número que você escolheu é \033[4mímpar')    