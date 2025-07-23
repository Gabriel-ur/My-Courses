ano = int(input('Qual ano deseja analisar? '))

if ano%4 == 0 and ano%100 != 0 or ano%400 == 0:
    print(f'\nO ano {ano} é \033[35mbissexto.\033[0m')
else:
    print(f'\nO ano {ano} \033[31mnão\033[0m é bissexto.')