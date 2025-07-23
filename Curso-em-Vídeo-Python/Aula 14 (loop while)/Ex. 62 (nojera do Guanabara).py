a1 = int(input('Digite o primeiro termo de uma progressão aritmética: '))
r = int(input('Qual a razão dessa PA: '))
t = a1
c = 1
tot = 0
n = 10

while n != 0:
    tot += n
    while c <= tot:
        print(f'{t}; ', end='')
        t += r
        c += 1
    print('PAUSA')
    n = int(input('\nQuantos termos a mais deseja mostrar: '))
print(f'PROCESSO FINALIZADO COM {tot} TERMOS MOSTRADOS.')