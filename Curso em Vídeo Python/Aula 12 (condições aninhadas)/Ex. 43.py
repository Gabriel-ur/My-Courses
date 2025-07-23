print('-=-' * 6)
print('CALCULADORA DE IMC')
print('-=-' * 6)

peso = float(input('\nSeu peso (kg): '))
altura = float(input('Sua altura (metros): '))

#esse if é pra caso o usuário digite em cm invés de m

if altura.is_integer:
    altura = altura / 100
imc = peso / altura **2

if imc <= 18.5:
    print(f'Seu imc é {imc:.2f}, portanto você está abaixo do peso.')
elif 18.5 < imc <= 25:
    print(f'Seu imc é {imc:.2f}, portanto você está na pesagem ideal.')
elif 25 < imc <= 30:
    print(f'Seu imc é {imc:.2f}, portanto você está acima do peso.')
elif 30 < imc <= 40:
    print(f'Seu imc é {imc:.2f}, portanto você está obeso.')
else:
    print(f'Seu imc é {imc:.2f}, portanto você está com obesidade mórbida.')