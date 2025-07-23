print('-=-' * 5)
print('PREÇO DE VIAGEM')
print('-=-' * 5)

km = float(input('\nQual a distância da viagem (km)? '))

if km <=200:
    print(f'Como a viagem é menor que 200km, o valor ficará em R${km*0.5:.2f}')
else:
    print(f'Como a viagem é maior que 200km, o valor ficará em R${km*0.45:.2f}')