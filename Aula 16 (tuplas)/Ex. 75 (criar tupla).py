numeros = tuple(int(input('Digite um número: '))for n in range(4))

print(f'O n° 9 apareceu {numeros.count(9)} vezes.')
print(f'O valor 3 foi digitado na posição {numeros.index(3)+1}' if 3 in numeros
      else '', end='')
print(f'Os valores pares digitados foram: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end ='; ')