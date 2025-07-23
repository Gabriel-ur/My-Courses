print('-=-' * 7)
print('ESSE TRIÂNGULO EXISTE?')
print('-=-' * 7)

l1 = float(input('\nMedida do 1° lado: '))
l2 = float(input('Medida do 2° lado: '))
l3 = float(input('Medida do 3° lado: '))

if l1+l2>l3 and l1+l3>l2 and l2+l3>l1:
    print('\nEba, esse triângulo existe!')
else:
    print('\nTá chapadão colega, não existe não')