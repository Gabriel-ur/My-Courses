#se colocar while 'true' ele roda infinitamente sem a necissidde de uma variável de controle
while True:
    u = input('Você gosta de mim? [s/n]: ')
    while u == 'n':
        u = input('Gosta sim >:( [s/n]: ')
    if u == 's':
        break
#o comando 'break' interrompe o loop

print('\nEu sabia que você gostava de mim ;)')