print('-=-' * 7)
print('SEQUÊNCIA DE FIBONACCI')
print('-=-' * 7)

n = int(input('Digite quantos elementos deseja saber: '))

a = 0
b = 1
c = 0

count = 0 
while count < n:
    count += 1
    a = b
    b = c
    c = a + b
    print(f'{c}; ', end='')