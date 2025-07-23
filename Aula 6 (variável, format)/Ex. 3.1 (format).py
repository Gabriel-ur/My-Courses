print('Bem vindo(a) à calculadora mais simples do universo! Nela, digite dois valores, que direi a soma destes')

n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))

s = n1 + n2

#o ".format" serve pra evitar o uso excessivo de vírgulas e afins, deixando o código mais leve e clean

print('A soma de {} e {} é {}!'.format(n1,n2,s))

### ATUALMENTE, USA-SE O FORMAT COM UM 'f' NA FRENTE DAS ASPAS. Exemplo:

nome = input('Qual seu nome? ')
print(f'Olá, {nome}!')