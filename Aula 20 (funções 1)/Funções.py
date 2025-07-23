#funções são blocos de código REUTILIZÁVEIS capazes de realizar determinada ação, como 'print()', 'int()'
#é possível criar as próprias funções dentro do Python
#todas as funções em python terminam em '()' 
#normalmente, funções são criadas para realizar algo que o programador julga repetitivo em seu programa

def mostra_linha():
    print('-' * 20)


mostra_linha()
print('Hello world!'.center(20))
mostra_linha()
print('Muito show'.center(20))
mostra_linha()
print('Adoro "def"!'.center(20))
mostra_linha()


def mensagem(msg): #o que tá entre parênteses se chama PARÂMETRO
    print('-=' * 10)
    print(msg)
    print('-=' * 10)


mensagem('    Muito louco')
mensagem('    Mão na roda')


def celsius_para_fahrenheit(temperatura):
    return ((temperatura * 1.8) + 32) #'return' retorna um valor, sendo possível armazená-lo em variável


temp = float(input('\nDigite graus em Celsius: '))
print(f'{temp}°C em Fahrenheit é {celsius_para_fahrenheit(temp)}°F\n')


def soma(a, b):
    return a + b
    

v1 = int(input('Valor 1: '))
v2 = int(input('Valor 2: '))
v3 = soma(v1, v2)

print(f'A soma de {v1} ("a") + {v2} ("b") é {v3} ("soma")')
#é possível especificar os valores de cada parâmetro, podendo inverter a ordem
v3 = soma(b=v1, a=v2)
print(f'Agora "a" é {v2} e "b" é {v1}, soma igual a {v3}\n')

#é possível desempacotar um parámetro

def count(* num): #o '*' serve pra basicamente jogar todos os parâmetros digitados nesse 'num'
    tamanho = len(num)
    print('Recebi os valores:\033[32m', end=' ')
    for val in num:
        print(val, end=' ')
    print(f'\033[0me são ao todo {tamanho} números.')

count(2, 3, 1, 6)
count(5, 9)
count(4, 6, 12)
