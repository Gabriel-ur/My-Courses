print('-=-' * 5)
print('CÁLCULO DE MÉDIA')
print('-=-' * 5)

nota1 = float(input('\nSua primeira nota: '))
nota2 = float(input('Sua segunda nota: '))
rep = float(input('Nota máxima para reprova: '))
rec = float(input('Nota máxima para recuperação: '))
media = (nota1 + nota2) / 2

if media < rep:
    print(f'\nComo sua média é \033[31m{media:.2f}\033[0m, você foi \033[31mREPROVADO\033[0m.')
elif rep <= media < rec:
    print(f'\nComo sua média é \033[33m{media:.2f}\033[0m, você está de \033[33mRECUPERAÇÃO\033[0m.')
elif media >= rec:
    print(f'\n\033[4mParabéns\033[0m, sua média é \033[34m{media:.2f}\033[0m e você foi \033[34mAPROVADO\033[34m.')