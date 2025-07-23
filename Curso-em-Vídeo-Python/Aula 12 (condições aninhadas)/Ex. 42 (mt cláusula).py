print('-=-' * 7)
print('QUE TRIÂNGULO É ESSE?')
print('-=-' * 7)

l1 = float(input('\nMedida do 1° lado: ')) 
l2 = float(input('Medida do 2° lado: ')) 
l3 = float(input('Medida do 3° lado: ')) 

if l1+l2>l3 and l1+l3>l2 and l2+l3>l1:

    #aqui, esse 'end' serve para mudar o que o python coloca no final da função
    #print sempre coloca um '\n' no final, então "end=''" significa trocar o '\n' por nada

    print('Este é um triângulo ', end='')
    if l1==l2==l3:
        print('\033[32mEQUILÁTERO\033[0m (todos os lados iguais).')
    elif l1!=l2!=l3!=l1:
        print('\033[31mESCALENO\033[0m (todos os lados diferentes).')
    else:
        print('\033[33mISÓCELES\033[0m (dois lados iguais).')
else:
    print('\033[3mNem triângulo isso é...\033[0m')