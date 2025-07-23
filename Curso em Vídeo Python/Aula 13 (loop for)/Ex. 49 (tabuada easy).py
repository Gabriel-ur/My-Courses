print('-=-' * 2)
print('TABUADA')
print('-=-' * 2)

n = int(input('\nQual número deseja saber a tabuada: '))
print()

for t in range(1, 11):
    print(f'{n} x {t} = {n*t}')