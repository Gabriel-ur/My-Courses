a1 = int(input('Qual o primeiro termo da PA: '))
r = int(input('Qual a razão dessa PA: '))

print('\nA sequência de termos dessa PA, do 1 ao 10, é:\n')
for a in range(a1, a1 + (r *10), r):
    print(f'{a} -> ', end = '')