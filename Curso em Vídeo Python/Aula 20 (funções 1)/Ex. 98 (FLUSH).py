from time import sleep

def contador(i, f, p):
    for c in range(i, f + 1, p):
        print(c, end=' ', flush=True) #sem o flush o programa n roda o sleep a cada iteração 
        sleep(0.3)
    print('-> Fim')


print('-=-' * 10)
print('Contagem de 1 a 10 de 1 em 1')
sleep(0.5)
contador(1, 10, 1)
print('-=-' * 10)

sleep(0.5)
print('Contagem de 10 a 0 de 2 em 2')
sleep(0.5)
contador(10, -1, -2)
print('-=-' * 10)

sleep(0.5)
print('Agora você vai criar a contagem!')
i = int(input('Início: '))
f = int(input('Fim:    '))
p = int(input('Passo:  '))

if p == 0:
    p += 1

sleep(0.5)
print('-=-' * 10)
print(f'Contagem de {i} a {f} de {abs(p)} em {abs(p)}')
sleep(0.5)

if f < i and p > 0:
    p = -p
if f > i and p < 0:
    p = abs(p)
if f < 0:
    f -= 2

contador(i, f, p)
print('-=-' * 10)