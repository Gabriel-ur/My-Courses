clubes = ('Botafogo', 'Flamengo', 'Fortaleza', 'Palmeiras',
          'Cruzeiro', 'São Paulo', 'Bahia', 'Athletico-PR',
          'Athletico-MG', 'Bragantino', 'Vasco da Gama',
          'Criciúma', 'Juventude', 'Grêmio', 'EC Vitória',
          'Internacional', 'Fluminense', 'Corinthians',
          'Cuiabá', 'Atlético-GO')

print('-=-' * 6)
print('TABELA BRASILEIRÃO')
print('-=-' * 6)

print(f'\n{clubes}\n')

print(f'\nOs 5 primeiros colocados são: \033[32m{clubes[0:5]}\033[0m')
print(f'Os últimos 4 colocados são: \033[31m{clubes[-4:]}\033[0m')
print(f'\nTodos os clubes em ordem alfabética: {sorted(clubes)}')
print(f'Palmeiras está na posição {clubes.index("Palmeiras")+1}ª')