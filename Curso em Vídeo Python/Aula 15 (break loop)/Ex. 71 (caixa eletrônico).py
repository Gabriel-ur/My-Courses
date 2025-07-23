cedula = 50
totcedula = 0

val = int(input('Quanto deseja sacar (valor inteiro): \033[32mR$'))
print()
total = val

while True:
    if total >= cedula:
        total -= cedula
        totcedula += 1
    else:
        if totcedula > 0:
            print(f'\033[0mTotal de {totcedula} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totcedula = 0
        if total == 0:
            break

#versão simplificada:

#total = int(input('digite um valor inteiro: '))
#for i in (50, 20, 10, 1):
#    tced = 0
#    while total >= i:
#        total -= i
#        tced += 1
#    if tced != 0:
#        print(f'Total de cédulas de R$ {i}: {tced}')