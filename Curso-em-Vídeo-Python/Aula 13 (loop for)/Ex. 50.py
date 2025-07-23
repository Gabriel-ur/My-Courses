v = int(input('Deseja ler quantos valores: '))
ip = input('Deseja ver os pares ou ímpares (\033[36mp\033[0m/\033[31mi\033[0m): ')

s = 0
c = 0

print()
for quant in range(v):
    n = int(input('Digite um número inteiro: '))
    if ip == 'p':
        if n%2 == 0:
            s += n
            c += 1
    elif ip == 'i':
        if n%2 != 0:
            s += n
            c += 1
if ip == 'p':
    print(f'\nA soma dos {c} números \033[4mPARES\033[0m que você digitou é {s}')
elif ip == 'i':
    print(f'\nA soma dos {c} números \033[4mÍMPARES\033[0m que você digitou é {s}')