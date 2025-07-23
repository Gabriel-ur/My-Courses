from time import sleep

print('-=-' * 4)
print('SUPER TABUADA')
print('-=-' * 4)
print('\n>>> para parar, digite um número negativo\n')

while True:
    n = int(input('Deseja saber a tabuada de qual número: '))
    if n < 0:
        break
    print()
    for t in range(1, 11):
        sleep(0.2)
        print(f'{n} x {t} = {n*t}')
    print()
    sleep(0.2)
sleep(0.5)
print('\nPROGRAMA ENCERRADO...')