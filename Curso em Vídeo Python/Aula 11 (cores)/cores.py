cor = {'nd':'\033[0m','negrito':'\033[1m','italico':'\033[3m','sublinhado':'\033[4m','preto':'033[30m','vermelho':'\033[31m','verde':'\033[32m','amarelo':'\033[33m','azul':'\033[34m','roxo':'\033[35m','ciano':'\033[36m','cinza':'\033[37m','branco':'\033[97m',}

sorriso = ':)'
print('\033[4;35;43mHello world!\033[0m')
print(f'Corzinha bonitinha \033[1;36m{sorriso}\n')

#pra colocar cor segue a fórmula "\033[...m", dentro das aspas do print/input/etc
#precisa colocar "\033[0m" no final pra resetar, se não o código inteiro fica colorido
#o 1° n° é o style do texto; o 2° n° é a cor; o 3° n° é a cor do fundo do texto; separados por ';'

#STYLE (0; 1 ... 8; 9):
print('\033[0mOlha quantos estilos diferentes\033[0m') #normal: 0
print('\033[1mOlha quantos estilos diferentes\033[0m') #negrito: 1
print('\033[2mOlha quantos estilos diferentes\033[0m') #escurecido: 2
print('\033[3mOlha quantos estilos diferentes\033[0m') #itálico: 3
print('\033[4mOlha quantos estilos diferentes\033[0m') #sublinhado: 4
print('\033[5mOlha quantos estilos diferentes\033[0m') #piscar lentamente: 5
print('\033[6mOlha quantos estilos diferentes\033[0m') #piscar rapidamente: 6
print('\033[7mOlha quantos estilos diferentes\033[0m') #inverte o fundo com a cor da letra: 7
print('\033[8mOlha quantos estilos diferentes\033[0m') #oculto: 8
print('\033[9mOlha quantos estilos diferentes\033[0m') #tachado: 9

#COR DA LETRA (30; 31 ... 36; 37; 97):

print('\n\033[30mSo many cores oh jesus\033[0m') #preto
print('\033[31mSo many cores oh jesus\033[0m') #vermelho
print('\033[32mSo many cores oh jesus\033[0m') #verde
print('\033[33mSo many cores oh jesus\033[0m') #amarelo
print('\033[34mSo many cores oh jesus\033[0m') #azul
print('\033[35mSo many cores oh jesus\033[0m') #roxo
print('\033[36mSo many cores oh jesus\033[0m') #ciano
print('\033[37mSo many cores oh jesus\033[0m') #cinza
print('\033[97mSo many cores oh jesus\033[0m') #branco

#COR DO FUNDO (40; 41 ... 46; 47; 107):

print('\n\033[40mSo many fundos oh jesus\033[0m') #preto
print('\033[41mSo many fundos oh jesus\033[0m') #vermelho
print('\033[42mSo many fundos oh jesus\033[0m') #verde
print('\033[43mSo many fundos oh jesus\033[0m') #amarelo
print('\033[44mSo many fundos oh jesus\033[0m') #azul
print('\033[45mSo many fundos oh jesus\033[0m') #roxo
print('\033[46mSo many fundos oh jesus\033[0m') #ciano
print('\033[47mSo many fundos oh jesus\033[0m') #cinza
print('\033[107mSo many fundos oh jesus\033[0m') #branco