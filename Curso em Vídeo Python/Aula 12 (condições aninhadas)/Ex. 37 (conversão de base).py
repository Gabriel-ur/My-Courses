print('-=-' * 6)
print('CONVERSOR DE BASE')
print('-=-' * 6)

n = int(input('\nDigite um número \033[4minteiro\033[0m: '))
conversao = int(input('''Qual base de conversão deseja?\n
[ 1 ] BINÁRIO
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL
\nOpção: '''))

if conversao == 1:
    print(f'\n{n} convertido em binário é \033[36m{bin(n)[2:]}\033[0m') #esse 2: serve pra n mostrar os primeiros dois digitos, que seriam "0b"
elif conversao == 2:
    print(f'\n{n} convertido em octal é \033[36m{oct(n)[2:]}\033[0m') #esse 2: serve pra n mostrar os primeiros dois digitos, que seriam "0o"
elif conversao == 3:
    print(f'\n{n} convertido em hexadecimal é \033[36m{hex(n)[2:]}\033[0m') #esse 2: serve pra n mostrar os primeiros dois digitos, que seriam "0x"
else:
    print('\nAlgo deu errado, tente novamente.')