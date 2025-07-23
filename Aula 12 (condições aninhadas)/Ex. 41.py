idade = int(input('Quantos anos você tem? '))

if idade <= 9:
    print('\nCategoria: \033[35mMIRIM\033[0m')
elif 9 < idade <= 14:
    print('\nCategoria: \033[36mINFANTIL\033[0m')
elif 14 < idade <= 19:
    print('\nCategoria: \033[34mJÚNIOR\033[0m')
elif 19 < idade <= 25:
    print('\nCategoria: \033[32mSÊNIOR\033[0m')
else:
    print('\nCategoria: \033[31mMASTER\033[0m')