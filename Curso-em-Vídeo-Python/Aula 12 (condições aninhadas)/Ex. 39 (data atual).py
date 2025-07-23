#datetime é uma módulo interna do python que serve para lidar com datas e horários
#ela pode pegar a data e hora do computador, criar datas, etc

from datetime import date

print('-=-' * 11)
print('SERVIÇO MILITAR (não chora jovem)')
print('-=-' * 11)

ano = int(input('\nEm que ano você nasceu? '))
idade = date.today().year - ano

if idade < 18:
    print(f'\n\033[36mRelaaaxa\033[0m, como você tem {idade} anos, ainda faltam {18 - idade} anos pro alistamento.\nSeu alistamento será em \033[4m{date.today().year + (18 - idade)}\033[0m')
elif idade > 18:
    print(f'\n\033[33mQUE ISSO SENHOR\033[0m, já se passaram {idade - 18} ano(s) da sua data de alistamento. \033[3mFica esperto...\033[0m\nSeu alistamento foi em \033[4m{date.today().year - (idade - 18)}\033[0m')
else:
    print(f'\n\033[31mKKKK\033[0m, vc tem {idade}, vai lá se alistar vai >:)')