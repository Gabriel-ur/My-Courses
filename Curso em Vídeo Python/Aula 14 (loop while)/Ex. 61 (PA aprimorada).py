a1 = int(input('Digite o primeiro termo de uma progressão aritmética: '))
r = int(input('Qual a razão dessa PA: '))
t = int(input('Deseja ver quantos termos (os primeiros): '))
n = a1 + r * (t-1)

print(f'\nOs 10 primeiros termos dessa PA são: {a1}; ', end='')
while a1 < n:
    a1 += r
    print(f'{a1}; ', end='')