print('LEITOR DE SOMA DE NÚMEROS')
print('Digite quantos números quiser e te direi a soma entre eles.')
print('>>>> para parar de contar, digite 999\n')

count = 0
soma = 0
n = ''

while n != 999:
    n = int(input('Digite um número: '))
    if n != 999:
        count += 1
        soma += n
print(f'\nA soma dos {count} valores que você digitou (tirando 999) é igual a {soma}')